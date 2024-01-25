import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):

    @pytest.mark.positive
    def test_create_booking_tc1(self):
        # URL, auth, Payload, Headers, Injson
        # response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
        #                          payload=payload_create_booking(), in_json=True)
        # print(response)
        # This is the response in dict format {'bookingid': 2787, 'booking': {'firstname': 'Amit', 'lastname': 'Gupta',
        # 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}}
        # verify_response_key_should_not_be_none(response["bookingid"])
        # Important --> above three line are not giving response in json so in_json = false
        # and convert the response in json in 3rd line
        payload = payload_create_booking()
        print(payload)
        print(type(payload))
        # response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
        #                          payload=payload, in_json=False)
        # print(response)
        # bookingid = response.json()["bookingid"]
        # print(bookingid)
        # verify_response_key_should_not_be_none(bookingid)
        # print(response.status_code)
        # verify_http_status_code(response.status_code, 200) # this will be reuse

    @pytest.mark.negative
    def test_create_booking_tc2(self):
        # Negative test with no paylaod --> 500 error ideally should be 400 payload = {} not None
        # URL, auth, Payload, Headers, Injson
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload={}, in_json=False)
        # print(response)
        # verify_response_key_should_not_be_none(response.json()["bookingid"])
        print(response.status_code)
        verify_http_status_code(response.status_code, 500) # this will be reuse
        # bookingid = response.json()["bookingid"]
        # print(bookingid)
