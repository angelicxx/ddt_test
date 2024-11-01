import pprint

import requests

from api_testing.base_request import BaseRequest

BASE_URL_JSONPLACE = 'https://jsonplaceholder.typicode.com/'
base_request = BaseRequest(BASE_URL_JSONPLACE)

jsplace_info = requests.get('https://jsonplaceholder.typicode.com/posts?userId=1')
pprint.pprint(jsplace_info)
pprint.pprint(jsplace_info.json())
pass