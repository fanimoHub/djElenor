---
title: Contributing
---

We welcome all contributions to djElenor, including issues, new features, docs, discussions, and more. Read the following document to learn more about the process of contributing.

## Issues

Use [GitHub Issues](https://github.com/fanimoHub/djElenor/issues) to report a bug or a problem that you found in djElenor. Use the "Bug report" issue template to provide information that will help us confirm the bug, such as steps to reproduce, expected behavior, djElenor version, and any additional context. When our team confirms a bug, it will be added to the internal backlog and picked up as soon as possible. When willing to fix a bug, let us know in the issue comment, and we will try to assist you on the way.

## New features
When willing to propose or add a new feature, we encourage you first to open a [discussion](https://github.com/fanimoHub/djElenor/discussions) or an [issue](https://github.com/fanimoHub/djElenor/issues) (using "Feature request" template) to discuss it with the core team. This process helps us decide if a feature is suitable for djElenor or design it before any implementation starts.

Before merging, any new pull requests submitted to djElenor have to be reviewed and approved by the core team. We review pull requests daily, but if a pull request requires more time or feedback from the team, it will be marked as "queued for review".

## Managing dependencies

### VENV

To guarantee repeatable installations, all project dependencies are managed using PIP. The project’s direct dependencies are listed in `requirements.txt`.




## Git commit messages

To speed up the review process and to keep the logs tidy, we recommend the following simple rules on how to write good commit messages:

### Summary line

- It should contain less than 50 characters. It is best to make it short
- Introduce what has changed, using imperatives: fix, add, modify, etc.

### Description

- Add extra explanation if you feel it will help others to understand the summary content
- If you want, use bullet points (each bullet beginning with a hyphen or an asterisk)
- Avoid writing in one line. Use line breaks so the reader does not have to scroll horizontally

*Tip*: To ease review, try to limit your commits to a single, self-contained issue. This will also help others to understand and manage them in the future.


For more information and tips on how to write good commit messages, see the GitHub [guide](https://github.com/erlang/otp/wiki/writing-good-commit-messages).
