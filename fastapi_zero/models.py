from sqlalchemy.orm import Mapped, registry
from datetime import datetime


table_registry = registry()

@table_registry.mapped_as_dataclass
class User:
    __table__ = 'users'

    id: Mapped[int]
    username: Mapped[str]
    email: Mapped[str]
    password:  Mapped[str]
    created_at: Mapped[datetime]