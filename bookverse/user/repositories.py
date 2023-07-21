from .repo_interface import IUserRepo
from ..app import db

from .models import User


class UserRepoSqlLite(IUserRepo):
    def create(self, name, email, password_hash):
        user = User(name, email, password_hash)
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, user_id, name, email, password_hash):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise Exception('User not found')
        user.name = name
        user.email = email
        user.password_hash = password_hash
        db.session.commit()
        return user

    def retrieve(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise Exception('User not found')
        return user

    def retrieve_by_email(self, email):
        users = User.query.filter_by(email=email).all()
        if not users:
            raise Exception('User not found')
        return users

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()

