import re
import shutil
import subprocess
from pathlib import Path


# --------------------------------------------------
# Configuration
# --------------------------------------------------

REPO_PATH = Path.cwd()

# Set to False if you want the script to organize
# files but NOT automatically push to GitHub.
AUTO_PUSH = True


# --------------------------------------------------
# Helper function to run Git commands
# --------------------------------------------------

def run_git(command):
    print(f"\n> {' '.join(command)}")

    result = subprocess.run(
        command,
        cwd=REPO_PATH,
        text=True
    )

    if result.returncode != 0:
        print("\nGit command failed.")
        raise SystemExit(1)


# --------------------------------------------------
# Check that this is a Git repository
# --------------------------------------------------

if not (REPO_PATH / ".git").exists():
    print("ERROR: This folder is not a Git repository.")
    print("Run this script from the root of your repository.")
    exit()


# --------------------------------------------------
# Find and move assignment files
# --------------------------------------------------

# Matches:
# Assignment16_1.py
# Assignment17_10.py
# Assignment25_3.py
#
# Captures:
# 16, 1
# 17, 10
# 25, 3

pattern = re.compile(
    r"^Assignment(\d+)_(\d+)\.py$",
    re.IGNORECASE
)

moved_files = []

for file in REPO_PATH.iterdir():

    # Only look at files in the repository root
    if not file.is_file():
        continue

    match = pattern.match(file.name)

    if not match:
        continue

    assignment_number = match.group(1)

    folder_name = f"Assignment{assignment_number}"
    assignment_folder = REPO_PATH / folder_name

    # Create folder if it doesn't exist
    assignment_folder.mkdir(exist_ok=True)

    destination = assignment_folder / file.name

    # Avoid overwriting an existing file
    if destination.exists():
        print(f"SKIPPED: {file.name}")
        print(f"       {destination} already exists.")
        continue

    shutil.move(str(file), str(destination))

    print(f"MOVED: {file.name} -> {folder_name}/{file.name}")

    moved_files.append(file.name)


# --------------------------------------------------
# Nothing to do
# --------------------------------------------------

if not moved_files:
    print("\nNo new assignment files needed organizing.")
    exit()


# --------------------------------------------------
# Git
# --------------------------------------------------

print(f"\nOrganized {len(moved_files)} file(s).")

run_git(["git", "add", "."])


# --------------------------------------------------
# Show staged changes
# --------------------------------------------------

print("\nGit changes:")
subprocess.run(
    ["git", "status", "--short"],
    cwd=REPO_PATH,
    text=True
)


# --------------------------------------------------
# Commit
# --------------------------------------------------

commit_message = "Organize assignment files into directories"

run_git([
    "git",
    "commit",
    "-m",
    commit_message
])


# --------------------------------------------------
# Push
# --------------------------------------------------

if AUTO_PUSH:
    run_git(["git", "push", "origin", "main"])

    print("\nSUCCESS!")
    print("Assignments organized and pushed to GitHub.")
else:
    print("\nFiles organized and committed.")
    print("AUTO_PUSH is disabled.")
    print("Run 'git push origin main' when ready.")