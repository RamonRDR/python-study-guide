# Git and Version Control Basics

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../05-packages-and-dependencies/README.md) · [Module index](../README.md) · [Next →](../../fundamentals/01-how-python-runs-a-program/README.md)
<!-- /chapter-navigation:top -->

## Goal

**Level:** absolute beginner. **Estimated time:** 30–45 minutes, excluding installation and account setup. Use a personal practice project, not a work repository. By the end, you can record and inspect a version of your Python code, and understand how to synchronize it with a remote repository.

Git is a version-control tool. It records snapshots (commits) of selected files so you can inspect changes and collaborate. GitHub and GitLab host Git repositories and add collaboration tools. Git works locally without an account or internet connection. A remote account is needed only for the optional publishing exercise.

## 1. Install and configure Git

Use the [official Git installation page](https://git-scm.com/install/). On Windows, install Git for Windows and reopen PowerShell or VS Code. On macOS, follow the documented installation options, including the Xcode command-line tools if appropriate. On Linux, use your distribution's official package manager.

```shell
git --version
```

In the terminal, open the existing python-practice folder. Check the current folder with Get-Location (PowerShell) or pwd (macOS/Linux). Run git status first. If it already belongs to a repository, use a new separate practice folder outside that repository; do not create a nested repository by accident. If Git reports that the folder is not a repository, initialize it:

```shell
git init -b main
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

Replace the illustrative identity with your preferred commit name and an appropriate email (a hosting provider's verified no-reply address is an option). These configuration commands affect this repository only. Commit names and emails are recorded in history; avoid exposing personal information. If your Git version does not recognize -b, update Git using the official installation instructions.

## 2. Decide what belongs in version control

Create a plain-text file named .gitignore at the project root (no .txt extension), containing:

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

These patterns exclude generated environments, Python caches and a common local configuration file. They do not protect files already tracked or remove secrets from history. Review every change; never commit credentials, private data, or a real .env file.

Keep first_program.py, .gitignore and the reviewed requirements.txt from Chapter 05. Do not commit .venv. If requirements.txt contains private URLs or local paths, correct it before staging.

## 3. Record the first commit

Run git status to inspect files. Stage only the intended files by name:

```shell
git add .gitignore first_program.py requirements.txt
git diff --cached
git status
git commit -m "feat: add first Python program"
git log --oneline
```

If you skipped the optional dependency exercise, create a reviewed requirements.txt containing only dependencies you actually need (an empty file is acceptable for the first program). A staged file is selected for the next commit. The commit records a snapshot and message locally. Nothing has been uploaded.

Change the message in first_program.py, save it and run it with your verified environment interpreter. Then inspect and commit:

```shell
git diff
git add first_program.py
git diff --cached
git commit -m "feat: update greeting"
git log --oneline
git status
```

You should see two commits and, if there are no other changes, a clean working tree. git diff shows unstaged changes; git diff --cached shows staged changes; git log shows history. If the result differs, inspect status instead of blindly repeating commands.

## 4. Understand remotes (optional practice)

A remote is a named connection to another repository. GitHub and GitLab offer different web interfaces but use the same basic Git commands. If you want to publish, create an empty repository on your chosen provider without an initial README, license or .gitignore. Prefer a private practice repository, check its visibility and contents, and follow the provider's authentication guidance. Never paste passwords or access tokens into a remote URL or commit.

Copy the HTTPS clone URL from your own repository. Replace the placeholder below before running the command:

```shell
git remote add origin YOUR_REPOSITORY_HTTPS_URL
git remote -v
git push -u origin main
```

If origin already exists, inspect it rather than overwriting it. The first push sends your local commits and configures the upstream branch. Authentication may open a browser or credential manager. If the remote already has history or push is rejected, stop and inspect the cause; do not force-push.

For subsequent updates, first ensure git status is clean and you are on the intended branch. In this simple single-branch practice repository:

```shell
git pull --ff-only
git log --oneline
```

pull obtains remote commits and integrates them; --ff-only refuses to create a merge when the histories have diverged. If it refuses, stop and ask for help instead of resetting or overwriting work. After a new reviewed local commit, git push publishes it. git clone copies an existing remote repository into a new folder; use it from outside the original repository:

```shell
git clone YOUR_REPOSITORY_HTTPS_URL python-practice-copy
```

Recreate the virtual environment from requirements.txt in the copy using Chapters 04–05; Git does not transfer the ignored .venv.

## 5. The professional workflow, briefly

In a shared project, a branch isolates a change, a pull request (GitHub) or merge request (GitLab) proposes it, review checks it, and CI runs automated checks. Merge integrates approved changes. Do not push directly to a protected shared main branch. The later engineering-practices material will apply these ideas to Python. Detailed branching, conflicts, history recovery, GitHub Actions, GitLab CI and collaboration belong to the planned independent Git Study Guide; no external course is required here.

## Practice and quick reference

- [ ] Verify Git and configure a practice repository.
- [ ] Create .gitignore and confirm .venv is not staged.
- [ ] Review and commit the first program, change it and commit again.
- [ ] Inspect the two commits and explain the difference between local commit and remote push.
- [ ] Optionally publish to your own empty practice repository and clone it into a separate folder.

If a command fails, read its message, verify the current folder, check git status and consult the official documentation. Do not use destructive reset, force-push or credential workarounds.

## Official references

- [Git installation](https://git-scm.com/install/)
- [Git basics: recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- [Git remote repositories](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [GitHub authentication](https://docs.github.com/en/authentication)
- [GitLab authentication](https://docs.gitlab.com/user/gitlab_com/#authentication)

<!-- chapter-navigation:bottom -->
[← Previous](../05-packages-and-dependencies/README.md) · [Module index](../README.md) · [Next →](../../fundamentals/01-how-python-runs-a-program/README.md)
<!-- /chapter-navigation:bottom -->
