# Git

## Onboarding

### What problem does this aim to solve?

Git is designed to tackle the complexities of tracking changes in software development projects. Before version control systems like Git, developers often found it challenging to keep track of changes in code, collaborate effectively without overwriting each other's work, and revert back to previous states of a project if needed. Git solves these problems by providing a robust, efficient system for version control and collaboration.

### What sub-category of technologies is this?

Git is a "Distributed Version Control System" (DVCS). Unlike centralized version control systems, every Git directory on every developer's computer is a full-fledged repository with a complete history and full version-tracking abilities, independent of network access or a central server. This approach greatly enhances the flexibility and speed of development workflows.

## Developer life with/without this tool

### Without Git

- **Tracking Changes**: Developers manually track changes in files, which is error-prone and lacks efficiency.
- **Collaboration**: Collaborating on a codebase is difficult. Changes by different team members can easily overwrite each other, leading to loss of work.
- **Reverting Changes**: Reverting to a previous version of the project is complex and sometimes impossible without a systematic backup.
- **Example Scenario**: A developer accidentally overwrites a file with an older version, losing all recent work because there is no record of the newer changes.

### With Git

- **Efficient Change Tracking**: Git allows developers to track every single change in the project, down to specific lines in files. Each change is part of a commit with a unique ID.
  - Example Command:

    ```bash
    git commit -m "Added new login feature"
    ```

- **Seamless Collaboration**: Multiple developers can work on the same project simultaneously without overwriting each other's work, thanks to branches and merging.
  - Example Command:

    ```bash
    git merge feature-branch
    ```

- **Safe Reversion**: Git enables safe and easy reversion to previous states without losing current progress.
  - Example Command:

    ```bash
    git revert <commit-hash>
    ```

- **Example Workflow**: A developer creates a new branch (`git branch new-feature`), works on new features, commits changes (`git commit -m "New feature added"`), and merges these changes back to the main branch (`git merge new-feature`).

## Core Concepts

### Repository (Repo)

A Git repository is where project files and their history are stored. It can be on your local machine or a remote server. Creating a new local repository involves running `git init`, while cloning an existing repository from a remote source uses `git clone <url>`.

### Commit

Commits are the core in Git's snapshot-based approach. Each commit represents a specific state of your repository. A commit includes a message describing the changes and is identified by a unique hash. You create a commit after staging changes with git add, encapsulating those changes in the repository’s history using `git commit -m "commit message"`.

### Branch

Branches in Git allow multiple streams of work to be carried out concurrently, diverging from the main codebase. Creating a new branch (`git branch <branch-name>`) enables development without impacting the main or 'master' branch, making it ideal for working on new features or experiments.

### Merge

Merging is the method of integrating changes from one branch into another, often from a feature branch back into the main branch. It's a critical process for combining completed work and is accomplished with the `git merge <branch-name>` command.

### Pull Request

Pull requests (PRs), primarily used in online Git repositories like GitHub, are proposals for merging one branch into another. They allow for code review and discussion before the changes are integrated, enhancing collaboration and code quality. PRs are created after pushing a branch to a remote repository and submitting a merge request through the platform's interface.

## Core APIs

### `git init`

- Purpose: Initializes a new Git repository in your current directory, setting up the necessary .git directory and metadata.
- Usage Example:

    ```bash
    mkdir MyProject
    cd MyProject
    # Initializes a new Git repository in the current directory
    git init
    ```

### `git clone`

- Purpose: Copies an existing Git repository, typically from a remote source like GitHub, to your local machine.
- Usage Example:

    ```bash
    # Clones the repository from GitHub to your local machine
    git clone https://github.com/username/repository.git
    ```

### `git add`

- Purpose: Stages changes in your working directory for the next commit.
- Usage Example:

    ```bash
    # Stages all current changes in the directory for the next commit
    git add .
    ```

### `git commit`

- Purpose: Records a snapshot of the staged changes in the repository history.
- Usage Example:

    ```bash
    # Commits the staged changes with a descriptive message
    git commit -m "Add new feature"
    ```

### `git push`

- Purpose: Uploads local repository content to a remote repository.
- Usage Example:

    ```bash
    # Pushes changes from your local main branch to the remote main branch
    git push origin main
    ```

## Small running example

### Installation

1. Install Git:

- For macOS: Use Homebrew with the command `brew install git`.
- For Windows: Download the Git installer from the Git [website](https://git-scm.com/download/win).
- For Linux: Install Git using your distribution's package manager, e.g., `sudo apt-get install git` for Ubuntu.

2. Verify Installation:

- Check if Git is installed by running `git --version` in your terminal or command prompt.

### Code

We'll go through the process of initializing a repository, making changes, and pushing them to a remote repository.

1. Initialize a Repository:

    ```bash
    # Create a new directory and initialize a Git repository
    mkdir MyProject
    cd MyProject
    git init
    ```

2. Create a File and Commit Changes:

    ```bash
    # Create a new file and add some content
    echo "Hello Git!" > hello.txt

    # Stage the file for commit
    git add hello.txt

    # Commit the file to the repository
    git commit -m "Initial commit with hello.txt"
    ```

3. Create a Remote Repository (Optional):

- Create a new repository on a platform like GitHub.
- Copy the remote repository URL.

4. Connect Your Local Repository to the Remote Repository:
    ```bash
    # Replace 'remote-repository-url' with the URL of your remote repository
    git remote add origin remote-repository-url
    ```

5. Push Changes to Remote Repository

    ```bash
    # Push the committed changes to the remote repository
    git push -u origin master
    ```

6. Check Status:

    ```bash
    # Check the status of your local repository
    git status
    ```

