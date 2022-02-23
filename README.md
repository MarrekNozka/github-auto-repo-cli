# Automated Repository Creation

An automation for GitHub repository creation,
both in GitHub and locally in your chosen path.

## Installation

You need to install the
[PyGithub](https://github.com/PyGithub/PyGithub) package.

```terminal
pip3 install PyGithub
```

or:

```terminal
pip install PyGithub
```

... and [`fzy`](https://github.com/jhawthorn/fzy) and `git`.

## Usage

1. After cloning the project:

* create [GitHub toke](https://github.com/settings/tokens) and edit `config.py`:

  ```python
  github_token = "ghp_.........................."
  ```

* and add your credentials.

2. Then, just run `python3 github-repo.py`

## Usage

`github-repo.py [org name [repo name]]`

* default `repo_name` is actual directory name
* `...` as `'org name'` mean interactive choice

``````
./github-repo.py 'org name'
./github-repo.py ...
./github-repo.py 'org name' repo_name
./github-repo.py ... repo_name
``````

## Tip

Create an alias for it in your `.zshrc` or `.bashrc`.
For example, in my case I created this:

```zsh
alias gh-repo="python3 ~/lib/github-repo-autocreate/github-repo.py"
```

or

```zsh
cd ~/.local/bin
ln -s ~/lib/github-repo-autocreate/github-repo.py gh-repo
```


So now whenever I type `gh-repo` in my terminal
I'm able to create the repo in just a few seconds.

## Thanks

This small project was possible with the help of the great package [PyGithub](https://github.com/PyGithub/PyGithub).
