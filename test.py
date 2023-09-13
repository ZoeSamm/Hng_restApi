import os
import requests


def test_create_task():
    url = 'http://localhost:5000/api'
    data = {'name': 'Oluwakemi'}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()['response'].endswith('created successfully')
    assert response.json()['id'] == 1
    assert response.json()['username'] is not None  # Updated assertion



def test_update_task():
    url = 'http://localhost:5000/api/1'
    data = {'name': 'Oluwakemi', 'username': 'ZoeSamm'}
    response = requests.put(url, json=data)
    assert response.status_code == 200
    assert response.json()['response'] == 'User update'
    assert response.json()['id'] == 1
    assert response.json()['name'] == 'Oluwakemi'
    assert response.json()['username'] == 'ZoeSamm'


def test_delete_task():
    url = 'http://localhost:5000/api/1'
    response = requests.delete(url)
    assert response.status_code == 204


def test_read_task_not_found():
    url = 'http://localhost:5000/api/100'
    response = requests.get(url)
    assert response.status_code == 404
    assert response.json()['response'] == 'No Result with id=100 Found'


def test_create_task_with_integer_in_name():
    url = 'http://localhost:5000/api'
    data = {'name': '123abc'}
    response = requests.post(url, json=data)
    assert response.status_code == 400
    assert response.json()['response'] == '123abc contains an integer, not allowed'


if __name__ == '__main__':
    test_create_task()
    test_update_task()
    test_delete_task()
    test_read_task_not_found()
    test_create_task_with_integer_in_name()
