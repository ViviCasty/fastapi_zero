import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi_zero.app import app
from fastapi_zero.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session  # sessão começa e termina / pausado

    table_registry.metadata.drop_all(engine)  # deleta tabelas apos testes

from sqlalchemy import event
from fastapi_zero.models import User

def _mock_db_time(model=User):

    def fake_time_hook(mapper, connection, target):
        print(target)
    event.listen(User, 'before_insert', fake_time_hook)

    yield time

    event.remove(User, 'before_insert', fake_time_hook)

