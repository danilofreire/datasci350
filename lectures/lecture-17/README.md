# Lecture 17 - Cloud Computing II

Last class you opened an AWS account and clicked around the console. This class you rent an actual machine, log into it from your own terminal, and run your code on it. By the end you will have launched a Linux server, moved files onto it, run a Jupyter notebook in the cloud, and terminated the whole thing so it costs you nothing.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-17/17-cloud2.html)

## What we cover

- EC2 instances, virtualisation, and how a hypervisor fits many machines onto one
- Ubuntu Server, and why we use the terminal rather than a desktop
- Launching an instance: choosing the Ubuntu 26.04 LTS image, a `t3.micro` type, a key pair, a security group, and a disk
- Which instance types your account can actually use for free, and why the console's own note is out of date
- Connecting over SSH, and the `chmod 400` that WSL users have to get right
- AWS CloudShell: a bash shell in the browser, the `aws` command line that comes signed in, and `dnf` instead of `apt`
- Using CloudShell to rescue a connection when the key permissions will not work on Windows
- Installing software with `apt`, including the `externally-managed-environment` error that stops `pip`
- Moving files two ways: `scp` from your laptop, and `wget` straight from the internet
- Port forwarding, so a notebook running on the instance opens in your own browser
- Stopping and terminating, and why the public IP address changes in between

Free-tier terms, instance types, package names and console screenshots were checked on 19 August 2026.

## What the free plan gives you

Accounts opened after 15 July 2025 do not get the old 750 free hours per month. Yours runs on credits: $100 at sign-up and up to $100 more, across six months. Instance hours are paid out of those credits, so an instance left running overnight costs you real money from a finite pot.

A `t3.micro` costs 0.0104 USD an hour. Left running for a month that is about $7.50 of your $100, and the disk keeps charging even while the instance is stopped.

Terminate everything before you close your laptop.

## The activities

Activity 01 installs Jupyter on the instance and forwards port 8888 to port 8000 on your machine.

Install the `jupyter-notebook` package, with a hyphen:

```bash
sudo apt install -y python3 python3-pip jupyter-notebook
```

Debian and Ubuntu split Jupyter in two. `python3-notebook` is the library on its own. It installs without error and leaves you with no `jupyter` command, so `jupyter notebook` fails. The `jupyter-notebook` package carries the command and pulls the library in with it.

Activity 02 runs a full analysis in the cloud. `weather_data.py` builds a small dataset on your laptop. You upload it with `scp`, download `weather_analysis.py` onto the instance with `wget`, run the analysis there, and bring `weather_analysis.png` back with `scp`. Both scripts live in this folder.

## Rendering

```bash
quarto render 17-cloud2.qmd
```

If Quarto cannot find Python, set `QUARTO_PYTHON=~/miniconda3/bin/python3` first.

## Before the next class

1. Terminate every instance you started in class.
2. Open the Billing and Cost Management console.
3. Check that your total is zero.
4. Read the final project instructions.

Next class we start on web APIs, which is how you will collect the data for your project.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
