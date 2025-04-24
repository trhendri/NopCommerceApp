# Selenium Hybrid Framework

## Python Selenium Pytest POM, HTML Reports

### Phases
1. Analyze application, technology & skill set of team, choose test cases
   - 100 TCs....
     - re-test cases (test data)
     - Regression cases
   - Test cases can be automated
   - 100% automation??

2. Design and implementation of the framework

3. Execution

4. Maintain (Version control system)


### eCommerce Application
 - Frontend - https://demo.nopcommerce.com/
 - Backend - https://admin-demo.nopcommerce.com/login

### Step 1: Create new Project and Install Required Packages
 - Selenium: Selenium Libraries
 - Pytest : Python UnitTest Framework
 - pytest-html: PyTest HTML Reports
 - pytest-xdist: Run Test Parallel
 - Openpyxl: MS Excel Support
 - Allure-pytest: to generate allure reports

### Step 2: Create Folder Structure

  **Project Name**
  - pageObjects(Package)
  - testCases(Pkg)
  - utilities(Pkg)
  - TestData(Folder)
  - Configurations(Fldr)
  - Logs (Fldr)
  - Screenshots (Fldr)
  - Reports (Fldr)
  - Run.bat

### Step 3: Automating Login Test Case
3.1: Create LoginPage Object Class under 'pageObjects'
3.2: Create LoginTest under "testCases"
3.3: Create conftest.py under "testCases" -can use fixtures for multiple tests

### Step 4: Capture screenshot on failure
4.1: Update Login Test with Screenshot under "testCases"

### Step 5: Read common values from ini file
5.1: Add "config.ini" file in "Configurations" folder - keep common data
5.2: Create "readProperties.py" utility file under utilities package to read common data
5.3: Replace hard coded values in Login test case

### Step 6:Adding logs to test case
6.1: Add customLogger.py under utilities packages
6.2: Add logs to Login test cases

### Step 7: Run Tests on Desired Browser/Cross Browser/Parallel
7.1: Update conftest.py with required Fixtures which will accept command line argument (browser)
7.2: Pass browser name as argument in command line

**To Run tests on desired browser**
pytest -s -v testCases/test_login.py -browser chrome
pytest -s -v testCases/test_login.py -browser firefox

**To Run Tests parallel**
pytest -s -v -n=3 testCases/test_login.py --browser chrome
pytest -s -v -n=3 testCases/test_login.py --browser firefox

## Step 8: Generate pytest HTML Reports
8.1: Update conftest.py with pytest hooks
8.2: To Generate HTML report run below command

pytest -s -v -n=3 --html=Reports\report.html testCases/test_login.py --browser chrome

## Step 9: Automating Data Driven Test Case
9.1: Prepare test data in Excel sheet; place the Excel file inside the TestData folder
9.2: Create "ExcelUtil.py" utility class under utilities package
9.3: Create LoginDataDrivenTest under testCases
9.4: Run the test cases

## Step 10: Adding new testcases

## Step 11: Grouping Tests
11.1: Grouping markers (Add markers to every test method)
@pytest.mark.sanity
@pytest.mark.regression

11.2: Add Marker entries in pytest.ini file
pytest.ini
____
 [pytest]
markers = 
    sanity
    regression

11.3: Select groups at run time
-m "sanity"
-m "regression"
-m "sanity and regression"
-m "sanity or regression"

Run Command
pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome

## Step 12: Run Tests in Command Prompt and run.bat file
12.1: Create run.bat file
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser Chrome
12.2: Open command prompt as Administrator and then run run.bat file

## Step 13: Rush the Code to Git and GitHub Repository


 
