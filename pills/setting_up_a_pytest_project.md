# Setting Up Pytest

_[A video demonstration is here.](https://youtu.be/zM-YTFlo1pI?t=0s)_

Learn to set up a new pytest project.

## What is pytest?

Pytest is a kind of programming tool called a test framework. It is written for
use with the programming language Python. We can use it to test that our systems
do what they are supposed to do. We can also use it to build our test-driving
practice.

## Prerequisites

Before we start you will need a few prerequisites. You may have installed these
before, but we'll check that they are all there to be sure you are set up well.

If you need reminding about these steps, what `pip` and `venv` are, or how to manage your dependencies - [refer back to this guide on package management with `pip` and `venv`.](https://github.com/makersacademy/python_foundations/blob/main/chapter1/challenges/package_management.md)

```shell
# Let's install pyenv, a tool to manage different versions of Python.
# This will ensure we have the latest Python, which has more readable error messages.
brew install pyenv
# You may be given some extra instructions at the end of the command.
# If you are, follow them. If not, keep going.

# Now we'll install the latest Python.
pyenv install 3.12

# And let's check to see if pip is properly installed
pip3 --version
# If you see "pip 24.X from /Users/..." then you can skip the next command.

# Otherwise, run these:
python3 -m ensurepip --upgrade

# Create a venv for this project and activate it
python3 -m venv golden_square_venv
source golden_square_venv/bin/activate

# If you have cloned this Golden Square repo 
# you should see a `requirements.txt` file
# Use it to install the necessary packages

(golden_square_venv) pip install -r requirements.txt

# If you can't see the requirements.txt file you can just install the libraries manually too.
(golden_square_venv) pip install pytest pytest-cov requests

# If you run into trouble here, contact your coach.
```

## Setting up a new project

To set up a new pytest project:

```shell
# First, create a directory for your project
mkdir your-project-directory
cd your-project-directory

# Create a venv for this project and activate it
python3 -m venv my_project_venv
source my_project_venv/bin/activate

# Next, install pytest using pip
(my_project_venv) pip install pytest 
# This may take a few minutes

# Create a folder for your testing files
(my_project_venv) mkdir tests
(my_project_venv) mkdir lib

# Create module init files in both `tests/` and `lib/` directories
(my_project_venv) touch tests/__init__.py
(my_project_venv) touch lib/__init__.py
# These might seem pointless, but they're important for Python to find
# all of your files.

# Verify your setup by running pytest
(my_project_venv) pytest
================================ test session starts ================================
platform darwin -- Python 3.1, pytest-7.2.0, pluggy-1.0.0
rootdir: .../your-project-directory
collected 0 items

=============================== no tests ran in 0.01s ===============================

# And create a repository for your changes
(my_project_venv) git init .
(my_project_venv) git add .
(my_project_venv) git commit -m "Project setup"

# Then go and create a repository on github.com
# On the next screen after you have created the repository,
# follow the "Push an existing repository from the command line" section
# To push your project to your github repository
# It will look something like this...
(my_project_venv) git remote add origin YOUR_REMOTE_ADDRESS
(my_project_venv) git branch -M main
(my_project_venv) git push -u origin main
```




<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
