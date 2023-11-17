# Replicate Python Starter

This is a starter project for users who want to use the [Replicate Python client](https://github.com/replicate/replicate-python) to run machine learning models in the cloud.

## Prerequisites
- You have installed python 3.8 or higher.
- You have a Replicate API token.

## Getting started
1. Clone this repository with `git clone git@github.com:replicate/python-starter.git`
2. Ensure virutalenv is installed with `pip install virtualenv`
3. Create a virtual environment with `virtualenv .venv`
4. Source the virtual environment with `source .venv/bin/activate` 
5. Install the dependencies with `pip install -r requirements.txt`
6. Add your Replicate API token by running `cp .env.example .env` and editing the `.env` file
7. Run the script with `python prediction.py`

## Contributing to This Project
To contribute to this project, follow these steps:

- Fork this repository.
- Create a branch: `git checkout -b <branch_name>`
- Make your changes and commit them: `git commit -m '<commit_message>'`
- Push to the original branch: `git push origin <project_name>/<location>`
- Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
