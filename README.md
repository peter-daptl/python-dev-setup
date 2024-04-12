# Initial Setup on Mac

* Install Xcode CLI - `xcode-select --install`
* Install Homebrew - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
* Install Pipenv (Python virtual machine and dependency installer) - `brew install pipenv`
	* Note any outputs with instructions on updating .zshrc or .bashrc to ensure appropriate installed commands are available from CLI
* Install Pyenv (manages multiple versions of Python) - `brew install pyenv`
	* Note any outputs with instructions on updating .zshrc or .bashrc to ensure appropriate installed commands are available from CLI
* Install Python versions 3.10 and 3.11 (Most code is deployed to Ubuntu, 22.04 uses 3.10, 24.04 uses 3.11) `pyenv install 3.10.0` `pyenv install 3.11.0`
* Not necessary, but recommend installing iterm2 and oh-my-zsh (terminal prettifier)
	* https://iterm2.com/
	* https://ohmyz.sh/
* Install docker-desktop https://www.docker.com/products/docker-desktop/

# Repository Defaults
Clone repository at https://github.com/peter-daptl/python-dev-setup

This repository contains:
* VS Code Profile with appropriate, and maybe too many, extensions, settings and configurations.

  Rather than detail each, you can select them in the VS Code extensions panel and see their descriptions.

* .gitignore - sample .gitignore file to use in repositories to prevent commiting unnecessary files

* .black - Black formatter configuration file. Used to set max line length to 100 vs the normal 80

* .flake8 - Flake8 Linter configuration file - used to set max complexity of methods, and to set line length to 100 for the Flake8 linter.

# Additional Helpful Ideas
* Install pre-commit - https://pre-commit.com/
* In any repository run `pre-commit install`
* add a pre-commit configuration file (.pre-commit-config.yaml) such as the one in the repository
	* this will run black, flake8 and other formatting and code cleanup tools upon commit, and prevent commit from happening till issues are addressed
		* Note: Some will be autofixed and need to be be re-added with the implemented changes.
		* Occasionally, pre-commit hooks can have conflicts, this is rare, but if so you can force commit by running `git commit --no-verify`
