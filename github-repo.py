#!/usr/bin/env python3

from sys import argv
import os
from config import github_token, default_method
from github import Github, BadCredentialsException, GithubException
from subprocess import run

NoneType = type(None)

gh = Github(github_token)


def create_repo(repo_name, org_name=None):
    try:
        user = gh.get_user()

        # create repo in user account
        if type(org_name) is NoneType:
            return user.create_repo(repo_name)
        else:
            orgs = {}
            orgs[f"{user.name:24} {user.html_url}"] = user

            for org in user.get_orgs():
                orgs[f"{org.name:24} {org.html_url}"] = org

            # create repo in org by choice
            if type(org_name) is bool and org_name:
                choices = "\n".join(orgs.keys())
                fzy = run(
                    ["fzy"],
                    input=choices.encode("utf8"),
                    capture_output=True,
                )
                choice = fzy.stdout.decode("utf8").strip()
                if choice:
                    return orgs[choice].create_repo(repo_name)
                else:
                    return None

            # create repo in org by name
            if type(org_name) is str:
                for name, org in orgs.items():
                    if org_name in name:
                        return org.create_repo(repo_name)
                return None

    except BadCredentialsException:
        print("\nOops, something is wrong with your credentials.")
    except GithubException:
        print(
            "\nOops, seems like you already have a GitHub repository"
            + " with that name."
        )


def get_dir_name():
    cwd = os.getcwd()
    return os.path.basename(cwd)


if __name__ == "__main__":
    if "-h" in argv[1:] or "--h" in argv[:1]:
        print(
            f"""
{argv[0]} [org name [repo name]]

USAGE:

* default repo_name is actual directory name
* ... in 'org name' mean interactive choice

{argv[0]} 'org name'
{argv[0]} ...
{argv[0]} 'org name' repo_name
{argv[0]} ... repo_name
"""
        )
        exit(0)

    args = len(argv[1:])
    if args == 0:
        org_name = None
        repo_name = get_dir_name()
    if args == 1 or args >= 2:
        if argv[1] == "...":
            org_name = True
        else:
            org_name = argv[1]
    if args == 1:
        repo_name = get_dir_name()
    if args >= 2:
        repo_name = argv[2]

    print(f"Repo name = '{repo_name}'")
    if type(org_name) is str:
        display_org_name = org_name
    else:
        display_org_name = ">>interactive select<<" if org_name else "<GitHub nick>"
    print(f"Org  name = '{display_org_name}'")

    answer = input("Continue? [Y/n] > ")
    if answer == "" or "Y" == answer.upper():
        if repo := create_repo(repo_name=repo_name, org_name=org_name):
            print()
            print(f"  Browser URL: {repo.html_url}")
            print(f"    clone URL: {repo.clone_url}")
            print(f"      SSH URL: {repo.ssh_url}")
            print(f"      Git URL: {repo.ssh_url}")
            print()

            print(">>> git init")
            run(["git", "init"])
            origin_name = input("Type origin branch name [origin] > ")
            if not origin_name:
                origin_name = "origin"

            origin_url = repo.ssh_url if default_method == "ssh" else repo.clone_url
            print(f"\n>>> git remote add {origin_name} {origin_url}")
            run(["git", "remote", "add", origin_name, origin_url])
            print()
            print("Maybe you want type ...")
            print("\tgit add .")
            print("\tgit commit -m Init")
            print(f"\tgit push -u {origin_name} main")
    else:
        print("Canceled")
        exit(0)
