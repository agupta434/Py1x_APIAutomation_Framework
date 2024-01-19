# HTTP Status verification

def verify_http_status_code(status_code, expected_status_code):
    # print(status_code)
    assert status_code == expected_status_code, "Expected HTTP Status Code" + str(expected_status_code)

def verify_json_key_for_not_null(key):
    assert key != "Key is non Empty"  + key
    assert key > 0, "Key is greater than zero"

def verify_response_key_should_not_be_none(key):
    assert key is not None

def verify_response_time():
    pass

# common verification
# HTTP Status code
# Headers
# Data Verification
# JSON Scheme
