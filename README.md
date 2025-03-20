# GitGhost 👻
A Python-based automation tool that haunts your Git history with automated commits! It generates and pushes commits over time, making it look like you've been active even when you're not.

 ## Features
- Automates multiple commits over a specified number of days.
- Randomly selects README content and commit messages from external files.
- Uses custom commit timestamps to simulate past activity.
- Pushes changes to a remote repository.


## Project Structure
```
    /gitghost
    │── readme_contents.txt   # Stores README update content
    │── commit_messages.txt   # Stores commit messages
    │── main.py               # Main script to automate commits
    │── README.md             # Documentation file
```


## Setup & Installation
### 1. Clone the Repository
   ```
   git clone https://github.com/aswnvm/gitghost.git
   cd gitghost
   ```

### 2. Install Dependencies
   Ensure you have Python installed, then install the required package:
   ```
   pip install gitpython
   ```

## Usage
```
python main.py
```
The script will prompt you for:

    Whether a local repo exists (y/n)
    GitHub username and repo details (if cloning)
    Number of days to commit
It will then automatically generate commits and push them to the repository.


## External Files
1. readme_contents.txt\
   Contains content that is added to the README.md file on every commit.

2. commit_messages.txt\
   Contains commit messages that are randomly selected for each commit.


## How It Works
- Clones the GitHub repository (or uses an existing local repo).\
- Reads commit messages and README content from external files\
- Generates commits over a specified number of days with different timestamps\
- Updates the README.md file with new content on each commit\
- Pushes the commits to the remote repository

> [!NOTE]
> Ensure that readme_contents.txt and commit_messages.txt contain relevant data.\
> The script modifies the README.md file, so use it on repositories where this is acceptable.\
> Push failures may occur if authentication issues arise; make sure you have the correct Git credentials set up.
