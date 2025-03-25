import git
from datetime import datetime, timedelta
from random import randint
import random
import os
import json
import re


def main():
    local_repo = input("local repo exists? (y/n): ").strip().lower()
    if local_repo == "n":
        username = input("Enter your username: ")
        repo_name = input("Enter the name of the repo: ")
        local_rep_path = input("Enter the destination path: ")
        repo = git.Repo.clone_from(
            f"https://github.com/{username}/{repo_name}.git", local_rep_path
        )
        print("repo cloned successfully!")
    else:
        local_rep_path = input("Enter the local repo path: ")
        repo = git.Repo(local_rep_path)
    print(local_rep_path)

    sel_file = file_list(local_rep_path)
    days = int(input("Enter the num of days to commit: "))

    for day in range(0, days):
        date = (datetime.today() - timedelta(days=day)).strftime("%Y-%m-%d %H:%M:%S")
        for i in range(0, randint(1, 5)):
            print(date)
            commit_n_push(os.path.join(local_rep_path, sel_file), repo, date)
    print("Commits done successfully!")


def file_list(dpath):
    files = [f for f in os.listdir(dpath) if os.path.isfile(os.path.join(dpath, f))]
    if not files:
        print("No files found in the directory.")
    else:
        print("\nAvailable Files:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

    try:
        choice = int(input("\nChooose the file you want to modify: ")) - 1

        if 0 <= choice < len(files):
            sel_file = files[choice]
            print(sel_file)
            return files[choice]
        else:
            print("\nInvalid selection.")
            return None
    except ValueError:
        print("\nInvalid input. Exiting...")
        return None


def json_load(jpath):
    with open(jpath, "r") as f:
        data = json.load(f)
    keys = list(data.keys())
    idx = random.randint(0, len(keys) - 1)
    dat = data[keys[idx]]
    return dat


def file_modifier(fpath, new_content, flag):
    with open(fpath, "r") as f:
        content = f.read()
    pattern = r'print\((["\'])(.*?)\1\)' if flag else r"[^.!?]+[.!?]"

    matches = re.findall(pattern, content)

    if matches:
        old_text = random.choice(matches)[1]
        if flag:
            new_cont = new_content.replace("\\", "\\\\")
            change = re.sub(
                rf'print\((["\']){re.escape(old_text)}\1\)',
                f"print({matches[0][0]}{new_cont}{matches[0][0]})",
                content,
                count=1,
            )
        else:
            change = content.replace(random.choice(matches), new_content, 1)
        with open(fpath, "w") as f:
            f.write(change)
        return True

    return False


def commit_n_push(fpath, repo, date):

    if os.path.splitext(fpath)[1] == ".py":
        flag = True
        json_f = "content_code.json"
    else:
        flag = False
        json_f = "content_readme.json"

    random_cont = json_load(json_f)
    modified = file_modifier(fpath, random_cont["text"], flag)

    if modified:
        repo.index.add([fpath])
        repo.index.commit(random_cont["commit_msg"], author_date=date, commit_date=date)
        repo.remotes.origin.push()
    else:
        print("No changes made. Skipping commit.")


if __name__ == "__main__":
    main()
