# Lecture 06 - More Git and GitHub

Working with other people: sending your commits to GitHub, pulling theirs back, and sorting out what happens when you both edit the same line.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-06/06-more-git-github.html)

## What we cover

- `git push` and `git pull`, and connecting a local repository to GitHub
- `.gitignore`, and what should never be committed
- Merge conflicts, and how to resolve one by hand
- Branches: creating, switching, merging, and deleting them
- Going back to an earlier commit safely
- `clone` versus `fork`, and how to keep a fork up to date
- Issues, pull requests, Gists, GitHub Pages, Actions, and the GitHub CLI

## Follow along

We carry on with the `my-project` repository from Lecture 05. If you do not have it, create a folder, run `git init`, and add a couple of files.

Your default branch may be called `master` or `main`. Both work identically, and the slides use `main`. Commit hashes in the screenshots are from my machine, so copy yours from `git log --oneline`.

A merge conflict looks alarming and is not. Git marks the disputed section with `<<<<<<<`, `=======`, and `>>>>>>>`. Delete the three marker lines and whichever text you do not want, then `add`, `commit`, and `push` as usual.

## Before the next class

1. Push your `my-project` repository to GitHub.
2. Create a branch, add a file to it, and merge it back.
3. Add a `.gitignore` file with at least one pattern in it.

Next time: `git diff`, amending and undoing commits, cherry-picking, and rebasing.

Many thanks to [Davi Moreira](https://davi-moreira.github.io) and [Simon Munzert](https://github.com/intro-to-data-science-21/lectures/tree/main) for sharing their materials, which I used as a basis for this lecture.
