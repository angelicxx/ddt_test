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


import pytest
import requests
from APIRoutes import APIRoutes

# 1. Проверка получения пивоварен по городу
@pytest.mark.parametrize('city', ['san_diego', 'new_york'])
def test_breweries_by_city(city):
    response = requests.get(APIRoutes.get_breweries_by_city(city))
    breweries = response.json()
    assert len(breweries) > 0, f"Пивоварни для города {city} не найдены!"
    for brewery in breweries:
        assert brewery['city'].lower().replace(' ', '_') == city, "Город в результате не совпадает!"

# 2. Проверка автозаполнения пивоварен
@pytest.mark.parametrize('query, expected', [('dog', 'Dog'), ('cat', 'Cat')])
def test_autocomplete_breweries(query, expected):
    response = requests.get(APIRoutes.autocomplete_breweries(query))
    results = response.json()
    assert len(results) > 0, f"Результаты для запроса '{query}' не найдены!"
    assert any(expected in result['name'] for result in results), f"'{expected}' отсутствует в результатах!"

# 3. Проверка случайных пивоварен
def test_random_breweries():
    response = requests.get(APIRoutes.get_random_breweries(size=3))
    breweries = response.json()
    assert len(breweries) == 3, "Количество случайных пивоварен не совпадает!"

# 4. Проверка поиска пивоварен по имени
@pytest.mark.parametrize('query', ['gordon', 'brew'])
def test_search_breweries(query):
    response = requests.get(APIRoutes.search_breweries(query))
    results = response.json()
    assert len(results) > 0, f"Пивоварни для запроса '{query}' не найдены!"
    assert any(query.lower() in result['name'].lower() for result in results), f"'{query}' отсутствует в результатах!"
