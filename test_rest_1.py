import requests

from api_testing.base_request import BaseRequest
import pprint
import pytest

BASE_URL_DOGAPI = 'https://dog.ceo/api/'
base_request = BaseRequest(BASE_URL_DOGAPI)

dog_info = requests.get('https://dog.ceo/api/breeds/list/all')
pprint.pprint(dog_info)
pprint.pprint(dog_info.json())
pass