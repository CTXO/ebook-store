from .repositories import UserRepoSqlLite
from .repositories import IUserRepo


class UserCrud:
    def __init__(self):
        self.repo: IUserRepo = UserRepoSqlLite()

    def create(self, name, email, password_hash):
        return self.repo.create(name, email, password_hash)

    def update(self, user_id, name, email, password_hash):
        return self.repo.update(user_id, name, email, password_hash)

    def retrieve(self, user_id):
        return self.repo.retrieve(user_id)

    def retrieve_by_email(self, email):
        try:
            return self.repo.retrieve_by_email(email)
        except:
            return None

    def delete(self, user_id):
        return self.repo.delete(user_id=user_id)
