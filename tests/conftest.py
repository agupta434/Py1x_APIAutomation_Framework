import pytest
import requests
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests,put_requests
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_token, payload_update_booking
from src.helpers.utils import common_headers_json,common_headers_put_patch_delete


@pytest.fixture(scope="session")
def create_token():  # this test no need to run as it is market as fixture
    response = post_requests(
        url=APIConstants.url_create_token(),
        headers=common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json=False
    )
    print(response)
    verify_http_status_code(response.status_code, 200)
    print(response.json())
    token = response.json()["token"]
    print(token)
    verify_response_key_should_not_be_none(token)
    return token


@pytest.fixture(scope="session")
def create_booking():
    payload = payload_create_booking()
    print(payload)
    response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                             payload=payload, in_json=False)
    print(response.json())
    bookingid = response.json()["bookingid"]
    print(bookingid)
    verify_response_key_should_not_be_none(bookingid)
    print(response.status_code)
    verify_http_status_code(response.status_code, 200)  # this will be reuse
    return bookingid
