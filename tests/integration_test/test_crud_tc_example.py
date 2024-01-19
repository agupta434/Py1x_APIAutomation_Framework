from src.constants.api_constants import Base_URL, base_url, APIConstants

print(Base_URL)
url = APIConstants.base_url()


def test_crud():
    print(Base_URL)

    url_direct_function = base_url()
    print(url_direct_function)

    url_class = APIConstants.base_url()
    print(url_class)
