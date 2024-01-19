# requests wrapper means to make post, put patch and delete
import json

import requests

# Http method Generic function
# option 1
# def get_request(url, auth):
#     response = requests.get(url=url, auth=auth)
#     return response
# def get_request_json(url, auth):
#     response = requests.get(url=url, auth=auth)
#     return response.json()

# option 2 these are generic function. anyone use these for test cases
def get_requests(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response

def post_requests(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def patch_requests(url, auth, headers, payload, in_json):
    patch_response_data = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


#json.dumps convert string to json
def put_requests(url, auth, headers, payload, in_json):
    put_response_data = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return put_response_data.json()
    return put_response_data

def delete_requests(url, auth, headers, payload, in_json):
    delete_response_data = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data
    
# data = get_requests("https://restful-booker.herokuapp.com/booking/1", in_json=True)
# # this data will be in json format if in-json = True, if false then return normal response

