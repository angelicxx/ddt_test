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

import pytest
import requests
from APIRoutes import APIRoutes

# 1. Проверка списка пород собак
breeds_response = requests.get(APIRoutes.get_dog_breeds())
breeds_data = breeds_response.json()['message']

@pytest.mark.parametrize('breed', ['bulldog', 'labrador', 'poodle'])
def test_dog_breeds_list(breed):
    assert breed in breeds_data, f"Порода {breed} не найдена в списке!"

# 2. Проверка случайного изображения собаки
random_image_response = requests.get(APIRoutes.get_random_dog_image())
random_image_data = random_image_response.json()['message']

def test_random_dog_image():
    assert random_image_data.startswith('https://'), "Ссылка на изображение некорректна!"

# 3. Проверка изображений для конкретной породы
@pytest.mark.parametrize('breed', ['bulldog', 'labrador'])
def test_images_by_breed(breed):
    response = requests.get(APIRoutes.get_dog_images_by_breed(breed))
    images = response.json()['message']
    assert len(images) > 0, f"Для породы {breed} изображения отсутствуют!"
    assert all(img.startswith('https://') for img in images[:5]), "Некорректные ссылки на изображения!"

# 4. Проверка доступности API
def test_api_status():
    assert breeds_response.status_code == 200, "API Dog Breeds недоступно!"
