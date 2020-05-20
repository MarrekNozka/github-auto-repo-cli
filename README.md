# Automated Repository Creation

An automation for GitHub repository creation,
both in GitHub and locally in your chosen path.

## Installation

The only thing you need to install is the
[PyGithub](https://github.com/PyGithub/PyGithub) package.

```terminal
pip3 install PyGithub
```

or:

```terminal
pip install PyGithub
```

## Usage

1. After cloning the project:

* edit `credentials.py`:

  ```python
  github_username = 'miLkBoi2'
  github_password = '1234helpme56'
  ```

* and add your credentials.

2. Then, just run `python3 app.py`

## Functionality Explanation

1. Running the script (`python3 app.py`)
2. You are asked where do you want the local repository to be created in
(absolute path).

  ```terminal
  [ABSOLUTE PATH]
  (for example: /home/jack/Desktop)
  (paths are case sensitive)
  
  > /home/mectos/Downloads
  ```

3. You are asked how do you want to name your repository.

  ```terminal
  [REPOSITORY NAME]
  > new_repo
  ```

4. Given that there were no errors in the process,
a new repository will be created both in GitHub and locally.

  ```terminal
  You have successfully created the repository new_repo
  Both locally and in Github.
  The local repository absolute path is /home/mectos/Downloads/new_repo
  ```


## Tip

Create an alias for it in your `.zshrc` or `.bashrc`.
For example, in my case I created this:

```zsh
alias repo="python3 ~/github/automated-repo-creation/app.py"
```

So now whenever I type `repo` in my terminal
I'm able to create the repo in just a few seconds.

## Thanks

This small project was possible with the help of the great package [PyGithub](https://github.com/PyGithub/PyGithub).
