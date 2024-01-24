# Python API Automation Framework

Hybrid Custom Framework to Test the REST APIs



### Tech Stack
1. Python 3.12
2. Requests - HTTP Requests
3. PyTest - Testing Framework
4. Reporting - Allure Report, PyTest HTML
5. Test Data - CSV, Excel, JSON
6. Parallel Execution - x distribute



### How to Install Packages
`` pip install requests pytest pytest-html faker allure-pytest jsonschema
``

### To Freeze your Package version
`` pip freeze > requirements.txt ``

## To Install the Freeze Version
``pip install -r requirements.txt``

## To run test 
``pytest tests/integration_test/test_create_booking.py -s -v --alluredir=./reports``
``pytest tests/datadriventesting/test_ddt.py --alluredir=reports``
  `` -s -v ``
## To open allure report 
``allure serve reports``
## To clean allure report 
``allure generate --clean``

## How to run your Testcase Parallel 
`` pip install pytest-xdist ``
`` pytest -n auto tests/integration_test/test_create_booking.py -s -v `` 


``pytest -n auto tests/integration_test/test_create_booking.py -s -v
``

### To Work with the Excel
``pip install openpyxl``


### To work wit JSON Schema
```pip install jsonschema```

### .gitignore creater for dotenv and pycharm+all
