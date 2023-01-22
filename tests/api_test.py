import pytest
from app import app

keys_post = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
}


def test_api_all_posts():
    """
    тест первого эндпоинта (значение - список, совпадение ключей)
    """
    response = app.test_client().get('api/posts/')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == list
    assert set(api_response[0].keys()) == keys_post


def test_api_post():
    """
    тест второго эндпоинта (значение - словарь, совпадение ключей)
    """
    response = app.test_client().get('api/posts/1')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == dict
    assert set(api_response.keys()) == keys_post
