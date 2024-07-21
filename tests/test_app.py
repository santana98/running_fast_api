from http import HTTPStatus


def test_read_root_return_ok_and_hello(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, world!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test_user',
            'email': 'teste@test.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'test_user',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'test_user',
                'email': 'teste@test.com',
                'id': 1,
            }
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'test_user',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_read_nonexistent_user(client):
    response = client.get('/users/100')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'test_user_test',
            'email': 'user@test.com',
            'password': 'password_test',
        },
    )

    assert response.json() == {
        'username': 'test_user_test',
        'email': 'user@test.com',
        'id': 1,
    }


def test_update_nonexistent_user(client):
    response = client.put(
        '/users/100',
        json={
            'username': 'test_user_test',
            'email': 'user@test.com',
            'password': 'password_test',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_nonexistent_user(client):
    response = client.delete('/users/100')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
