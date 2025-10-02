from fastapi_zero.models import User


def test_create_user():
    user = User(username='test', email='test@gamil.com', password='secrets')
    assert user.username == 'test'
