# Git Foundations

## Objective

Establish the local Git repository, connect it to GitHub, and understand the core Git workflow before beginning application development.

## Repository Setup

Local repository:

`<PROJECTS_DIR>\Secure-DevDecOps-Platform`

Remote repository:

The local repository is connected to the project's GitHub repository through the `origin` remote.

## Concepts Practiced

### Git vs GitHub

Git is the local distributed version-control system.

GitHub hosts the remote repository and provides collaboration features such as pull requests, issues, code review, and CI/CD through GitHub Actions.

### Working Directory

Files currently present or modified on the local filesystem.

### Staging Area

The staging area contains the exact snapshot of changes that will be included in the next commit.

A file is staged with:

```bash
git add <file>
```

### Local Repository

A commit stores a snapshot of staged changes in the local Git repository.

### Remote Repository

The remote named `origin` points to the GitHub repository.

The configured remote can be viewed with:

```bash
git remote -v
```

## Commands Used

```bash
git --version
git config --global user.name
git config --global user.email
git status
git remote -v
git branch
git rev-parse --show-toplevel
git diff
git diff --staged
git add .gitignore
```

## Troubleshooting

While moving the repository between local drives, PowerShell reported that the source `.git` directory could not be removed.

The move occurred across filesystems, so the repository was copied to the destination before Windows attempted to remove the original source.

The destination repository was verified using:

```bash
git status
git remote -v
git rev-parse --show-toplevel
```

This confirmed that the Git metadata and remote configuration were intact.

## Security Notes

The `.gitignore` file prevents common secrets, environment files, generated files, logs, and local development artifacts from being committed unintentionally.

`.gitignore` does not remove secrets that have already entered Git history, so secrets should be prevented from being committed in the first place.

Public project documentation should avoid exposing local usernames, machine names, personal email addresses, credentials, tokens, and unnecessary workstation-specific paths.

## Interview Takeaway

Git uses a multi-stage workflow:

```text
Working Directory
        ↓
     git add
        ↓
Staging Area
        ↓
   git commit
        ↓
Local Repository
        ↓
    git push
        ↓
Remote Repository
```

Understanding the staging area makes it possible to control exactly which changes are included in each commit.