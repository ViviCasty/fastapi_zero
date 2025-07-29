from http import HTTPStatus


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
        '/users/',
        json={
            'username': 'Alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'alice@example.com',
        'username': 'Alice',
    }
