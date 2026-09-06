"""Compute final grades for DATASCI 350 from a Canvas gradebook export.

Two modes:
    Stage 1 (default): list missing or non-numeric items per student
    Stage 2 (--compute): apply syllabus weights and rubric, write final-grades CSV

Usage:
    uv run --with pandas python datasci350_grades.py path/to/grades.csv
    uv run --with pandas python datasci350_grades.py path/to/grades.csv --compute
    uv run --with pandas python datasci350_grades.py ~/Desktop/grades.csv --compute --output ~/Desktop/final.csv

By default both outputs (the missing-items report and the final-grades CSV)
go into the same directory as the input file.

Course configuration (assignment count, quiz count, weights, rubric) is
hardcoded at the top of this file. Edit those constants if the syllabus changes.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

ASSIGNMENT_PREFIXES = [f"Assignment {i:02d}" for i in range(1, 11)]
QUIZ_PREFIXES = [f"Quiz {i:02d}" for i in range(1, 6)]
PROJECT_PREFIX = "Final project"

WEIGHTS = {"assignments": 0.50, "quizzes": 0.30, "project": 0.20}

# DATASCI 350 grading scale (syllabus.qmd, "Grading Scale" section).
# Lower bound -> letter, checked highest-first against the rounded final score.
LETTER_THRESHOLDS = [
    (93, "A"),
    (90, "A-"),
    (87, "B+"),
    (83, "B"),
    (80, "B-"),
    (77, "C+"),
    (73, "C"),
    (70, "C-"),
    (67, "D+"),
    (60, "D"),
    (0, "F"),
]

OUTPUT_BASENAME = "datasci350-final-grades.csv"
REPORT_BASENAME = "datasci350-missing-report.txt"


def find_columns(df: pd.DataFrame, prefixes: list[str]) -> list[str]:
    cols = []
    for prefix in prefixes:
        matches = [c for c in df.columns if c.startswith(prefix)]
        if len(matches) != 1:
            raise SystemExit(
                f"Expected exactly one column starting with {prefix!r}, got {matches}"
            )
        cols.append(matches[0])
    return cols


def split_points_possible(df: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    is_pp = df["Student"].astype(str).str.strip() == "Points Possible"
    if is_pp.sum() != 1:
        raise SystemExit(
            f"Expected exactly one 'Points Possible' row, found {is_pp.sum()}"
        )
    points = df.loc[is_pp].iloc[0]
    rest = df.loc[~is_pp].reset_index(drop=True)
    return points, rest


def drop_canvas_metadata(df: pd.DataFrame) -> pd.DataFrame:
    student = df["Student"].astype(str).str.strip()
    is_metadata = df["Student"].isna() | (student == "") | (student == "nan")
    is_test = student == "Student, Test"
    keep = ~(is_metadata | is_test)
    return df.loc[keep].reset_index(drop=True)


def parse_score(value) -> tuple[bool, str]:
    if pd.isna(value):
        return True, "<blank>"
    s = str(value).strip()
    if s == "":
        return True, "<blank>"
    try:
        float(s)
        return False, s
    except ValueError:
        return True, s


def inspect_missing(students: pd.DataFrame, item_cols: list[str], report_path: Path, input_name: str) -> None:
    lines: list[str] = []
    students_with_missing = 0
    item_missing_counts: dict[str, int] = {c: 0 for c in item_cols}

    for _, row in students.iterrows():
        per_student: list[tuple[str, str]] = []
        for c in item_cols:
            missing, raw = parse_score(row[c])
            if missing:
                per_student.append((c, raw))
                item_missing_counts[c] += 1
        if per_student:
            students_with_missing += 1
            lines.append(f"{row['Student']} (ID {row['ID']}):")
            for col, raw in per_student:
                lines.append(f"    - {col}: {raw}")
            lines.append("")

    header = [
        "DATASCI 350 - missing-items report",
        f"Input: {input_name}",
        f"Total real students: {len(students)}",
        f"Students with at least one missing item: {students_with_missing}",
        "",
        "Missing count per item:",
    ]
    any_missing = False
    for c in item_cols:
        if item_missing_counts[c]:
            header.append(f"    - {c}: {item_missing_counts[c]}")
            any_missing = True
    if not any_missing:
        header.append("    (none)")
    header.append("")

    body = lines if lines else ["No missing items found across all real students."]
    report = "\n".join(header + ["Per-student detail:", ""] + body)

    print(report)
    report_path.write_text(report)
    print(f"Report written to {report_path}")


def letter_grade(score: int) -> str:
    for threshold, letter in LETTER_THRESHOLDS:
        if score >= threshold:
            return letter
    return "F"


def assert_letter_grade_works() -> None:
    cases = [
        (100, "A"), (93, "A"), (92, "A-"), (90, "A-"),
        (89, "B+"), (87, "B+"), (86, "B"), (83, "B"),
        (82, "B-"), (80, "B-"), (79, "C+"), (77, "C+"),
        (76, "C"), (73, "C"), (72, "C-"), (70, "C-"),
        (69, "D+"), (67, "D+"), (66, "D"), (60, "D"),
        (59, "F"), (0, "F"),
    ]
    for score, expected in cases:
        actual = letter_grade(score)
        if actual != expected:
            raise SystemExit(f"letter_grade({score}) = {actual!r}, expected {expected!r}")


def cell_to_percent(value, points_possible: float) -> float:
    if pd.isna(value):
        return 0.0
    s = str(value).strip()
    if s == "":
        return 0.0
    try:
        raw = float(s)
    except ValueError:
        return 0.0
    if points_possible <= 0:
        return 0.0
    return raw / points_possible * 100.0


def compute_grades(
    students: pd.DataFrame,
    points: pd.Series,
    assignment_cols: list[str],
    quiz_cols: list[str],
    project_col: str,
) -> pd.DataFrame:
    pp = {c: float(points[c]) for c in assignment_cols + quiz_cols + [project_col]}

    rows = []
    for _, row in students.iterrows():
        a_pcts = [cell_to_percent(row[c], pp[c]) for c in assignment_cols]
        q_pcts = [cell_to_percent(row[c], pp[c]) for c in quiz_cols]
        p_pct = cell_to_percent(row[project_col], pp[project_col])

        a_avg = sum(a_pcts) / len(a_pcts)
        q_avg = sum(q_pcts) / len(q_pcts)

        weighted = (
            WEIGHTS["assignments"] * a_avg
            + WEIGHTS["quizzes"] * q_avg
            + WEIGHTS["project"] * p_pct
        )
        weighted_capped = min(weighted, 100.0)
        final = int(weighted_capped + 0.5)  # round half up, matches grading convention

        rows.append(
            {
                "Student": row["Student"],
                "ID": row["ID"],
                "Section": row.get("Section", ""),
                "Assignments avg": round(a_avg, 2),
                "Quizzes avg": round(q_avg, 2),
                "Project": round(p_pct, 2),
                "Weighted total": round(weighted_capped, 2),
                "Final score": final,
                "Letter grade": letter_grade(final),
            }
        )
    return pd.DataFrame(rows)


def compare_to_canvas(students: pd.DataFrame, computed: pd.DataFrame) -> list[str]:
    notes = []
    canvas_col = "Final Score"
    if canvas_col not in students.columns:
        return ["(no Canvas Final Score column found, skipping comparison)"]
    for i, row in students.iterrows():
        try:
            canvas = float(row[canvas_col])
        except (TypeError, ValueError):
            continue
        ours = float(computed.iloc[i]["Weighted total"])
        if abs(ours - canvas) > 0.5:
            notes.append(
                f"  - {row['Student']} (ID {row['ID']}): ours={ours:.2f}, "
                f"canvas={canvas:.2f}, diff={ours - canvas:+.2f}"
            )
    return notes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input", type=Path, help="path to the Canvas grade export CSV")
    parser.add_argument(
        "--compute",
        action="store_true",
        help="compute final grades (default: inspect missing items only)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=f"final-grades CSV path (default: <input-dir>/{OUTPUT_BASENAME})",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help=f"missing-items report path (default: <input-dir>/{REPORT_BASENAME})",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    input_csv = args.input.expanduser().resolve()
    if not input_csv.is_file():
        raise SystemExit(f"Input CSV not found: {input_csv}")

    output_csv = (args.output or input_csv.parent / OUTPUT_BASENAME).expanduser().resolve()
    report_txt = (args.report or input_csv.parent / REPORT_BASENAME).expanduser().resolve()

    df = pd.read_csv(input_csv, dtype=str)
    points_possible, rest = split_points_possible(df)
    students = drop_canvas_metadata(rest)

    assignment_cols = find_columns(students, ASSIGNMENT_PREFIXES)
    quiz_cols = find_columns(students, QUIZ_PREFIXES)
    project_col = find_columns(students, [PROJECT_PREFIX])[0]
    item_cols = assignment_cols + quiz_cols + [project_col]

    if not args.compute:
        inspect_missing(students, item_cols, report_txt, input_csv.name)
        return

    assert_letter_grade_works()
    computed = compute_grades(
        students, points_possible, assignment_cols, quiz_cols, project_col
    )
    computed.to_csv(output_csv, index=False)

    print(f"Wrote {len(computed)} rows to {output_csv}")
    print()
    print("Letter-grade distribution:")
    dist = computed["Letter grade"].value_counts()
    order = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    for letter in order:
        n = int(dist.get(letter, 0))
        bar = "#" * n
        print(f"    {letter:>3}: {n:>2}  {bar}")
    print()
    print("Score summary:")
    print(f"    min: {computed['Final score'].min()}")
    print(f"    median: {computed['Final score'].median():.1f}")
    print(f"    mean: {computed['Final score'].mean():.2f}")
    print(f"    max: {computed['Final score'].max()}")
    print()
    print("Diffs vs Canvas Final Score (only listed if abs diff > 0.5):")
    diffs = compare_to_canvas(students, computed)
    if diffs:
        for line in diffs:
            print(line)
    else:
        print("    (none, our totals match Canvas to within 0.5 points)")


if __name__ == "__main__":
    main()
