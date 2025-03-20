import git
from datetime import datetime, timedelta
from random import randint
import random
import os


def main():
    local_repo = input("local repo exists? (y/n): ").strip().lower()
    if local_repo == "n":
        username = input("Enter your username: ")
        repo_name = input("Enter the name of the repository: ")
        local_rep_path = input("Enter the destination path: ")
        repo = git.Repo.clone_from(
            f"https://github.com/{username}/{repo_name}.git", local_rep_path
        )
        print("repository cloned successfully!")
    else:
        local_rep_path = input("Enter the local repository path: ")
        repo = git.Repo(local_rep_path)
    print(local_rep_path)
    days = int(input("Enter the number of days to commit: "))
    for day in range(0, days):
        date = (datetime.today() - timedelta(days=day)).strftime("%Y-%m-%d %H:%M:%S")
        for i in range(0, randint(1, 5)):
            print(date)
            commit_n_push(local_rep_path, repo, date)
    print("Commits done successfully!")


def load_file_content(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def commit_n_push(local_rep_path, repo, date):
    readme_cont = load_file_content("readme_contents.txt")
    commit_msg = load_file_content("commit_messages.txt")

    random_readme_cont = random.choice(readme_cont)
    random_commit_msg = random.choice(commit_msg)
    with open(os.path.join(local_rep_path + "/README.md"), "w") as f:
        # f.write(f"This is a README file for the repository. Updated at {date}\n")
        f.write(f"{random_readme_cont} {date}\n")

    repo.index.add([os.path.join(local_rep_path + "/README.md")])
    repo.index.commit(random_commit_msg, author_date=date, commit_date=date)
    repo.remotes.origin.push()


if __name__ == "__main__":
    main()
