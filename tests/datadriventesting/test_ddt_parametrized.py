# Read the csv or excel file
# Create a function create_token and verify the expected result

# read CSV or excel file
import openpyxl
import requests
import pytest
from src.helpers.utils import common_headers_json
from src.constants.api_constants import APIConstants


# Read the file

def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
        print(credentials)
    # print(credentials)
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password,
    }
    # payload is not imported as it is changing dynamically
    response = requests.post(url=APIConstants.url_create_token(), headers=common_headers_json(), json=payload)
    print(response)
    return response

@pytest.mark.parametrize("user_cred", read_credentials_from_excel(r"Y:\8_API_Python\Py1x_APIAutomation_Framework\tests\datadriventesting\testddt_ddt.xlsx"))
def test_post_create_token(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    response = make_request_auth(username, password)
    print(response)
    assert response.status_code == 200
