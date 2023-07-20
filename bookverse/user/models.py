from ..database import Base
import sqlalchemy as sa


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    password_hash = sa.Column(sa.String(50), nullable=False)
    email = sa.Column(sa.String(50), nullable=False, unique=True)

    def __init__(self, name, email, password_hash):
        self.name = name
        self.password_hash = password_hash
        self.email = email
