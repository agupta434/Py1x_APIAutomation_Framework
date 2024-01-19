def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 222,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-01"
        },
        "additionalneeds": "Lunch"
    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123",
    }
    return payload

def payload_update_booking():
    payload = {
        "firstname": "Amit",
        "lastname": "Gupta",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload
