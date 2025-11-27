from http import HTTPStatus

from fastapi_zero.schemas import UserPublic


def test_root_deve_retornar_ola_mundo(client):
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - executa a coisa (o SUT)
    - A: Assert - Garante que A é A
    """
    # Arrange
    # TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Oi Momoi'}
    assert response.status_code == HTTPStatus.OK


def teste_exercicio_ola_mundo_em_html(client):
    response = client.get('/exercicio-html')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo no html </h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_create_user_already_exist(client, user):
    # user_schema = UserPublic.model_validate(user).model_dump()
    #UserPublic.model_validate(user).model_dump()
    response = client.post(
        '/users',
        json={
            'username': user.username,
            'email': 'testezin@test.com',
            'password': 'testtest1',
        },
    )
    assert response.status_code == HTTPStatus.CONFLICT
    assert 'Username already exists' in response.text


def test_create_email_already_exist(client, user):
    #UserPublic.model_validate(user).model_dump()
    response = client.post(
        '/users',
        json={
            'username': 'Ana',
            'email': user.email,
            'password': 'anatest',
        },
    )
    # breakpoint()
    assert response.status_code == HTTPStatus.CONFLICT
    assert 'Email already exists' in response.text


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_read_one_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


def test_read_one_user_not_found(client):
    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert 'User not found' in response.text


def test_update_integrity_error(client, user):
    # Criando um registro para "fausto"
    client.post(
        '/users',
        json={
            'username': 'fausto',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )

    # Alterando o user.username das fixture para fausto
    response_update = client.put(
        f'/users/{user.id}',
        json={
            'username': 'fausto',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {
        'detail': 'Username or Email already exists'
    }


def test_delete_user(client, user):
    UserPublic.model_validate(user).model_dump()

    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/1')
    # breakpoint()
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert 'User not found' in response.text
