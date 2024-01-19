import pytest
from tests.conftest import create_token, create_booking
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests, put_requests
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_token, payload_update_booking
from src.helpers.utils import common_headers_json, common_headers_put_patch_delete


class TestCRUD(object):

    def test_update_booking(self, create_token, create_booking):  # token or auth and bookingID from create booking
        # print(test_create_token)
        # print(test_create_booking)
        bookingID = str(create_booking)

        put_url = APIConstants.url_create_booking() + "/" + bookingID
        # no need of token if authorization is there
        headers = common_headers_put_patch_delete()  # authorization is Base64 code and after converting it will be admin and password123
        print(headers)
        auth = ("admin", "password123")
        response = put_requests(url=put_url, auth=None, headers=headers,
                                payload=payload_update_booking(), in_json=False)
        print(response.json())
        # bookingid = response.json()["bookingid"]
        # print(bookingid)
        # verify_response_key_should_not_be_none(response.json()["bookingid"])
        print(response.status_code)
        verify_http_status_code(response.status_code, 200)  # this will be reuse

    def test_delete_booking(self, create_token, create_booking):  # token, and bookingID from create booking
        bookingID = str(create_booking)
        put_url = APIConstants.url_create_booking() + "/" + bookingID
        # no need of token if authorization is there
        headers = common_headers_put_patch_delete()  # authorization is Base64 code and after converting it will be admin and password123
        auth = ("admin", "password123")
        response = put_requests(url=put_url, auth=None, headers=headers,
                                payload={}, in_json=False)
        print(response.json())
        # bookingid = response.json()["bookingid"]
        # print(bookingid)
        # verify_response_key_should_not_be_none(response.json()["bookingid"])
        print(response.status_code)
        verify_http_status_code(response.status_code, 200)  # this will be reuse
