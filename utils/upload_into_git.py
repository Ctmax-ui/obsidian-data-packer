import os
import subprocess
from datetime import datetime

def gitCommiter(path):
    repo_path = os.path.abspath(path or "output")
    commit_message = datetime.now().strftime("%d-%m-%Y-backup")

    def run_git_command(command):
        """Runs a Git command and prints the output."""
        result = subprocess.run(command, cwd=repo_path, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)

    if not os.path.exists(os.path.join(repo_path, ".git")):
        print("Initializing a new Git repository...")
        run_git_command("git init")

    # run_git_command('git config --global user.name "Your Name"')
    # run_git_command('git config --global user.email "your.email@example.com"')

    run_git_command("git add .")
    run_git_command(f'git commit -m "{commit_message}"')
    run_git_command("git push origin main")

    print("✅ Backup successfully pushed to GitHub!")
