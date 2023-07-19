from .repositories import UserRepoSqlLite

class UserCrud:
    def __init__(self):
        self.repo = UserRepoSqlLite()  # maybe change this to a factory

    def create(self, name, username, email, password_hash):
        return self.repo.create(name, username, email, password_hash)

    def update(self, user_id, name, username, email, password_hash):
        return self.repo.update(user_id, name, username, email, password_hash)

    def retrieve(self, user_id):
        return self.repo.retrieve(user_id)

    def delete(self, user_id):
        return self.repo.delete(user_id=user_id)
