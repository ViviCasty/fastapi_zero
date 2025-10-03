from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models import User

from datetime import datetime


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User, time=datetime.now()) as time:
        new_user = User(
            username='test', email='test@gmail.com', password='secrets'
        )
        session.add(new_user)  # sessão é uma transição e adiciona o user
        session.commit()  # uma operação só/mais leve

        user = session.scalar(
            select(User).where(User.username == 'test')
        )  # pedindo resultado da operação, retorna escalar ou um objeto python
        # resultado da instancia

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'email': 'test@gmail.com',
        'password': 'secrets',
        'created_at': time,
    }
