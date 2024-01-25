from dotenv import load_dotenv
import os

def test_auth():
    load_dotenv()
    usename = os.getenv("NAME")
    password = os.getenv("PASSWORD")
    print(usename,password)