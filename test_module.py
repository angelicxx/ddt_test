import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        '--base-url', action='store', default='https://ya.ru', help='Base URL for the API tests', status_code=200
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption('--base-url')


def test_api_endpoint(base_url):
    response = requests.get(f'{base_url}')
    print(response.request.url)
    assert response.status_code == 200

