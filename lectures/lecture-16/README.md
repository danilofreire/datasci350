# Lecture 16 - Introduction to Cloud Computing

Every computer in this course has been yours so far. This lecture rents someone else's: what a cloud provider actually sells, why anyone buys it, and how to open an AWS account without ever receiving a bill.

[View the slides](https://danilofreire.github.io/datasci350/lectures/lecture-16/16-cloud.html)

## What we cover

- Cloud computing as on-demand rental, and the four service types: IaaS, PaaS, SaaS, FaaS
- The costs a company avoids by renting, and what it gives up in exchange
- Two newsroom stories: Animoto scaling to 3,500 machines, and The Washington Post reading 17,481 pages in nine hours for $144.62
- Virtualisation and middleware, the two ideas the whole industry sits on
- The AWS catalogue: EC2, auto scaling and load balancers, S3, EBS and EFS, RDS, SageMaker AI
- The October 2025 outage: a race condition, an empty DNS record, and fifteen hours of broken internet
- Opening an account on the free plan, and setting a zero-spend budget
- Amazon Textract, reading a scanned document the way the Post did in 2008

Tool claims, prices and console screenshots were checked on 18 August 2026.

## Before class

Warning: AWS asks for a payment card, even on the free plan. Do this at home, not in class.

1. Open <https://aws.amazon.com/free/>.
2. Create the account with a personal email address.
3. Choose the **free plan** when asked. It ends after six months or when the credits run out, and it cannot become a bill.
4. Open the Billing and Cost Management console.
5. Create a zero-spend budget from the template. Add an email address you read.

The account starts with $100 in credits, and the console offers up to $100 more for trying services. Everything this course asks of you fits inside that.

## The document

`data/clinton-schedule-2001-pages-11-20.pdf` holds ten pages of Hillary Clinton's 2001 schedule, from the Clinton Presidential Library. It is the same kind of scanned, typewritten paper the Post fed through OCR, complete with redaction boxes and stray marks. We hand it to Textract and read what comes back.

The best moment is on page 8. Textract returns the header as "SCHEDULE FOR HILLARY RODAHM CLINTON", and that spelling is correct: the typist made the mistake in 2001. Anyone searching the archive for "Rodham" walks straight past the page.

The appendix keeps the older walkthrough for Amazon Transcribe, which turns audio into text the same way. You need it for the homework.

## Before the next class

1. Finish the account and the budget if you have not.
2. Windows users, install WSL. Tutorial 06 has the steps.
3. Check that `ssh` runs in your terminal.

Next class we launch an EC2 instance and log into it. Quiz 03 covers the AI module and this cloud module.

## Using AI in this course

You may use AI for the assignments in this course. Cite the tool you used, check everything it gives you, and remember that the fluency of an answer tells you nothing about whether it is correct.

Using AI tools in a manner prohibited in this course syllabus constitutes Cheating under the Emory Honour Code and is thus a form of academic misconduct.
