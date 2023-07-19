from bookverse.user.repo_interface import IUserRepo
from bookverse.database import db_session

from .models import User


class UserRepoSqlLite(IUserRepo):
    def create(self, name, username, email, password_hash):
        user = User(name, username, email, password_hash)
        db_session.add(user)
        db_session.commit()
        return user

    def update(self, user_id, name, username, email, password_hash):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise Exception('User not found')
        user.name = name
        user.username = username
        user.email = email
        user.password_hash = password_hash
        db_session.commit()
        return user

    def retrieve(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise Exception('User not found')
        return user

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        db_session.delete(user)
        db_session.commit()

