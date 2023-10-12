# Template Repo for organizing projects

This repository serves as an example of how to structure files and directories, 
particularly for R&D projects that encompass the construction of the end product.


# Setup
- Create venv using `conda create -n project-name python=3.11.5`
- Activate the venv and install poetry using `pip install poetry`
- Initialize the repo structure using `poetry new project-name --name project`
- Create [.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)


# Project Structure

```
project-name
|-- docs                    <- create datasets.md, papers.md, ... if needed
|   |-- diagrams
|   |   `-- workflow.md     <- use `mermaid` graphs so it will render in Github
|   `-- documentation.md
|-- project
|   |-- src                 <- src should be self contained and shouldn't rely on scripts/
|   |   |-- utils.py        <- place utility functions here and use in scripts/task1, ...
|   |   `-- __main__.py
|   |-- tests
|   |   `-- test_main.py
|-- scripts                 <- development workspace to try things out
|   |-- task1
|   `-- task2
|-- .gitignore
|-- LICENSE
|-- poetry.lock
|-- pyproject.toml
`-- README.md
```


# Principles
- Make each function do one thing well
- Make it easy to write, test and run programs
- Expect the output of every script to become the input to another, as yet unknown, script
- Clean code is better than clever code
- Use docstrings, type hints and follow [PEP8](https://pep8.org/) / [pyguide](https://google.github.io/styleguide/pyguide.html), [Zen of Python](https://peps.python.org/pep-0020/)
- Write comments to explain `why` and not `what`


# [Optional] Principles
- Integrate [black](https://black.readthedocs.io) and [mypy](https://mypy-lang.org) if required
- Implement [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow) for brancing strategy
- Use [Semantic Versioning](https://semver.org) or [Calendar Versioning](https://calver.org)
- Maintain a CHANGELOG.md to track the changes
- Utilize Github Issues and Github Projects to make your project workflow AGILE


# Note
I like organizing files, such as `project/src` and `project/tests`, as it 
simplifies the process of creating a .exe with PyInstaller. Additionally, 
having the tests directory inside the `project` folder facilitates the 
creation of a related `project2` within the same repository.
