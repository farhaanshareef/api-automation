# API Automation with Python

## Overview

This repository contains API automation tests using Python. The tests cover CRUD operations (Create, Read, Update, Delete) for a sample API. The automation suite is designed to run tests and generate detailed HTML reports for easy review.

## Prerequisites

- **Python Version**: Python 3.8 or higher is required for running the tests.
- **IDE**: PyCharm IDE is recommended for development and testing.

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

### 2. Install Dependencies

Install the required Python packages using the requirements.txt file:
pip install -r requirements.txt

### 3. Configure PyCharm
Open PyCharm.
Open the Project: Go to File > Open and select the project directory.
Set Up Interpreter: Go to File > Settings > Project: <project_name> > Python Interpreter, and select the virtual environment you created.
Run Configuration: You can create run configurations for different test scripts if needed.

API Automation
Test Files
The API automation suite is divided into several test files, each focusing on different types of API requests:

tests/post_user.py: Contains tests for creating a user.
tests/update_user.py: Contains tests for updating a user.
tests/patch_user.py: Contains tests for partially updating a user.
tests/delete_user.py: Contains tests for deleting a user.
tests/get_users.py: Contains tests for retrieving user data.
Smoke Suite
The smoke_suite.py file runs all the critical tests in sequence and generates an HTML report. The tests are executed in the following order:

Create User Test: Tests user creation.
Update User Test: Tests updating user information.
Patch User Test: Tests partial updates to user information.
Delete User Test: Tests user deletion.
Get User Test: Tests retrieval of user data.
Running the Tests
To run the full suite and generate an HTML report:
python smoke_suite.py --html= report/report.html
