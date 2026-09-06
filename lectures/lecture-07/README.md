# Lecture 07 - More Git Commands, CLI and Git Practice

The Git commands you reach for once the basics stop being enough: seeing what changed, fixing mistakes, moving commits around, and parking work you are not ready to commit.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-07/07-practice.html)

## What we cover

- `git diff`, and how to read its output
- `git commit --amend`, to fix the commit you just made
- `git reset`, and the difference between `--soft`, `--mixed`, and `--hard`
- `git cherry-pick`, to take one commit from a branch without merging all of it
- `git rebase`, including interactive rebase
- `git stash`, for setting work aside without committing it
- GitHub CLI (`gh`): installing it, authenticating, and working with repositories, issues, and pull requests

## A rule worth remembering

`--amend`, `reset --hard`, and `rebase` all rewrite history. That is fine on commits still sitting on your machine, and a problem once they have been pushed somewhere other people work from. Rewrite freely before you push, and use `git revert` afterwards.

## Practice

The deck ends with a ten-step quiz covering most of the term's Git material, from `init` to reading the log. Solutions are in the appendix slides. Try it before looking, since it is a good rehearsal for Quiz 01.

## Before the next class

1. Work through the practice quiz.
2. Install GitHub CLI and run `gh auth login`. Copy the install command from [cli.github.com](https://cli.github.com/) rather than typing it.
3. Make a list of anything that is still unclear.

Next class is the Quiz 01 review session. Bring your questions.

Many thanks to [Davi Moreira](https://davi-moreira.github.io) and [Simon Munzert](https://github.com/intro-to-data-science-21/lectures/tree/main) for sharing their materials, which I used as a basis for this lecture.
