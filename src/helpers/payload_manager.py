from faker import Faker
import json

faker = Faker()
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

# for dynamic install faker
def payload_create_booking_dynamic():
    json_payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.randon_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            # "checkin": str(faker.date_between(start_date='-3y', end_date='today')),
            "checkin": "2023-01-01",
            "checkout": "2023-01-01"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "WiFi", "Extra Bed"))
    }
    return json_payload


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
