import pytest
import requests

from api_testing.base_request import BaseRequest
import pprint

BASE_URL_BREWERYDB = 'https://api.openbrewerydb.org/v1/'
base_request = BaseRequest(BASE_URL_BREWERYDB)


brewery_city_1 = requests.get('https://api.openbrewerydb.org/v1/breweries?by_city=san_diego&per_page=3')
pprint.pprint(brewery_city_1.json())


@pytest.mark.parametrize('param', [0, 1, 2])
def test_city(param):
    assert brewery_city_1.json()[param]['city'] == 'San Diego'


brewery_city_2 = requests.get('https://api.openbrewerydb.org/v1/breweries/random?size=3')
pprint.pprint(brewery_city_2)


def test_random():
    assert 3 == len(brewery_city_2.json())


brewery_city_3 = requests.get('https://api.openbrewerydb.org/v1/breweries/search?query=dog&per_page=3')
pprint.pprint(brewery_city_3)


@pytest.mark.parametrize('param', [0, 1, 2])
def test_search(param):
    assert 'Dog' or 'Dogs' == brewery_city_3.json()[param]['name'].split(' ')[1]


brewery_city_4 = requests.get('https://api.openbrewerydb.org/v1/breweries/autocomplete?query=cat')
pprint.pprint(brewery_city_4)


def test_cat():
    assert 0 < len(brewery_city_4.json()) < 15


brewery_city_5 = requests.get('https://api.openbrewerydb.org/v1/breweries/search?query=dog&per_page=3')
pprint.pprint(brewery_city_5)


@pytest.mark.parametrize('param', [0, 1, 2])
def test_dog(param):
    assert 'Cat' != brewery_city_5.json()[param]['name'].split(' ')[1]


