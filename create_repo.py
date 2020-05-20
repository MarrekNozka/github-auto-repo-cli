import os
from credentials import github_username, github_password
from github import Github, BadCredentialsException, GithubException

username = github_username
password = github_password
gh = Github(username, password)


def create_repo(abs_path, repo_name):
    repo_path = os.path.join(abs_path, repo_name)
    try:
        os.mkdir(repo_path)
        try:
            user = gh.get_user()
            user.create_repo(repo_name)
            print("\nYou have successfully created the repository " +
                  f"{repo_name}\nBoth locally and in Github.\n" +
                  f"The local repository absolute path is {repo_path}\n")
        except BadCredentialsException:
            print("\nOops, something is wrong with your credentials.")
        except GithubException:
            print("\nOops, seems like you already have a GitHub repository" +
                  " with that name.")
    except FileNotFoundError:
        print(f"\nCouldn't find the directory provided ({abs_path})")
    except FileExistsError:
        print("\nThe directory provided already exists.")
