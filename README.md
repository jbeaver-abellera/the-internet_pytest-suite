<a id="title"></a>
# Test Practice on Heroku's the-internet App
This project explores Quality Assurance and automated testing techniques using the Page Object Model (POM). This is created to demonstrate how to structure and build automated tests to maintain web application effectively. This project focuses on testing Heroku's the-internet app which provides a variety of pages with common elements in websites. 

## Table of contents
- [Test Practice on Heroku's the-internet App](#test-practice-on-herokus-the-internet-app)
  - [Table of contents](#table-of-contents)
  - [Tech Stack:](#tech-stack)
  - [Usage](#usage)
  - [Tested Pages](#tested-pages)
  - [Project Structure](#project-structure)
  - [Github Workflow](#github-workflow)
  - [Pytest](#pytest)
      - [Filtering Tests](#filtering-tests)

<a id="tech-stack"></a>
## Tech Stack:
1. Programming Language - `python`
2. Testing Library - `pytest`
3. Automation Library - `Selenium`
4. Reporting Format - `JUnit`
5. CICD Platform - `Github Actions/Workflow`

<a id="usage"></a>
## Usage
To replicate a collaborative development environment, GitHub Workflows is setup to automate remote test runs whenever an individual pushes or creates a pull request to the repository. \
\
Additionally, an ad-hoc test run of the workflow can be performed using the following steps.
1. In the repository home, click on the 'Actions' tab of the repository and navigate to the 'test' workflow. You will then find previous runs of the test cases. 
<p align="center">
  <img src="https://github.com/jbeaver-abellera/the-internet_pytest-suite/assets/108796284/a2994f5f-c96b-41cc-a72b-c0e732ae380a" height="250">
</p>
2. From the list of workflow runs, click the name of the run to see details and other options.
<p align="center">
<img src="https://github.com/jbeaver-abellera/the-internet_pytest-suite/assets/108796284/ee131857-4b54-40ae-b233-3ed03050c8e2" alt="Go to Run" width="750">
</p>
3. In the upper-right corner of the workflow, re-run all jobs. If a prompt asks to rerun, just click Re-run jobs. 
<p align="center">
<img src="https://github.com/jbeaver-abellera/the-internet_pytest-suite/assets/108796284/986e5d84-4eb6-4dae-b179-caeffc419b96" alt="Rerun Jobs" width="750">
</p>
4. Once all the jobs are finished, go to the Artifact section below to download the test reports.
<p align="center">
<img src="https://github.com/jbeaver-abellera/the-internet_pytest-suite/assets/108796284/a6f50730-28e6-4aee-b622-d22ae844487d" alt="Go to Artifacts" width="750">
</p>
> You can also view details on the job by clicking on the job name in the left pane under 'jobs' section.
<p align="center">
<img src="https://github.com/jbeaver-abellera/the-internet_pytest-suite/assets/108796284/33d2de70-35c1-4af0-8054-8486c01c8486" alt="Go to Job" height="250">
</p>

<a id="tested-pages"></a>
## Tested Pages 
This automated test covers several key pages of the website. Including:
* `Add/Remove Elements Page` - The user must be able to create elements, and be able to delete them as well.
* `Broken Image Page` - All images in the page must be visible. Confirmed by accessing the image links.
* `Dropdown Page` - All the expected options should be visible in the page.
* `Dynamic Controls Page` - A test suite must be able to test asynchronously changing elements. 
* `Login Page` - Appropriate notification should appear on incorrect or correct login credentials.
  
<a id="project-structure"></a>
## Project Structure
This project follows an organized structure for automated UI testing projects. Here is a brief description of structure.
* **Root Folder**
   Contains subdirectories and configuration files for the project. This includes a gitignore, readme, requirements.txt for dependencies, pytest's conftest.py, etc.
* **utils/**
  Directory of python objects that are helpful for project files. This includes a constants file, and WebDriverSingleton() that ensures driver is created and closed only once.
* **PageClasses/**
  Directory of classes of pages that is tested by this project. A POM model is implemented for the web application, to create reusable and separated code for each pages.
* **tests/**
  Has all the files for testing the web app. Due to the nature of the website, test will be conducted for each page, instead of mimicking user interaction like buying an item.
* **junit/**
  Contains test results
* **.github/**
   Contains all the configuration for the testing pipeline in Github Workflow CI/CD.  
    
<a id="workflow"></a>
## Github Workflow
For this project, CICD platform Github Workflow is used for automated testing of the webpage. See below for how it is setup:
1. **Trigger Workflow**: The workflow will be run at every push or pull request to the main branch.
2. **Setup Environment**: To tell github workflow the configuration of the environment such as the OS, and to use the docker image for Selenium. 
3. **Code Checkout**: The workflow will checkout the files in this repository, as well as setup python and the required libraries.
4. **Test Executon**: It will now run the test usng pytest along wiith some options such as handling warnings and capturing results.
5. **Uploading Results**: When the tests are complete, the workflow will locate the test results and upload them to the 'Artifacts' section of the job run.

<a id="pytest"></a>
## Pytest
**Pytest** is a powerful python testing framework that can simplify running tests. It supports fixtures or annotation for setup and teardown, has various assertion methods, and support for various plugins. Pytest is widely used both for small project and large enterprise testing.

#### Filtering Tests
You can also filter tests using options in the 'pytest' command.
* **Keyboard Matching**: Use '-k' to run test matching a specific keyword. The command below can run any pytest function that has keywords 'header' or 'footer'.
``` bash
pytest -k "header and footer"
```    
* **Run by markers**: Use -m to run tests by marker names. 
``` bash
pytest -k "positive"
```    
Or
``` bash
pytest -k "negative"
```
> Just make sure to have your test functions marked like below.

``` python
pytest.mark.positve
def test_correctLoginCreds():
```
