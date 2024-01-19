# common Headers

def common_headers_json():
    headers = {
        "Content-Type": "application/json",
    }
    return headers
def common_headers_put_patch_delete():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
    }  # authorization is Base64 code and after converting it will be admin and password123
    return headers

def common_headers_xml():
    headers = {
        "Content-Type": "application/xml"
    }
    return headers

# Read data from Excel, json, YAML - Keep the common function here
