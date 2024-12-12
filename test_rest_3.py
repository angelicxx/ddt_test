import pprint

import requests

from api_testing.base_request import BaseRequest

BASE_URL_JSONPLACE = 'https://jsonplaceholder.typicode.com/'
base_request = BaseRequest(BASE_URL_JSONPLACE)

jsplace_info = requests.get('https://jsonplaceholder.typicode.com/posts?userId=1')
pprint.pprint(jsplace_info)
pprint.pprint(jsplace_info.json())
pass

import pytest
import requests
from APIRoutes import APIRoutes

# 1. Проверка постов по пользователю
user_posts_response = requests.get(APIRoutes.get_posts_by_user(1))
user_posts_data = user_posts_response.json()

@pytest.mark.parametrize('post_index', [0, 1, 2])
def test_user_posts(post_index):
    assert user_posts_data[post_index]['userId'] == 1, f"Пост {post_index} не принадлежит пользователю 1!"

# 2. Проверка постов по заголовку
post_title_response = requests.get(APIRoutes.get_posts_by_title('qui est esse'))
post_title_data = post_title_response.json()

def test_post_title():
    assert len(post_title_data) > 0, "Пост с заголовком 'qui est esse' не найден!"
    assert post_title_data[0]['title'] == 'qui est esse', "Заголовок поста не совпадает!"

# 3
post_body_response = requests.get(APIRoutes.get_posts_by_user(1))  # 
post_body_data = post_body_response.json()

def test_post_body():
    assert len(post_body_data) > 0, "Посты для пользователя с ID 1 не найдены!"


# 4. Проверка поста по ID
post_id_response = requests.get(APIRoutes.get_post_by_id(1))
post_id_data = post_id_response.json()

def test_post_by_id():
    assert post_id_data['id'] == 1, "ID поста не совпадает!"
