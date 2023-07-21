from .repositories import UserLibraryRepoSqlLite

class LibraryCrud:
    def __init__(self):
        self.repo = UserLibraryRepoSqlLite()

    def create_library(self, user_id):
        return self.repo.create_library(user_id)

    def list_ebooks(self, user_id):
        return self.repo.list_ebooks(user_id)