from .repositories import UserLibraryRepoSqlLite
from .repo_interface import IUserLibraryRepo


class LibraryCrud:
    def __init__(self):
        self.repo: IUserLibraryRepo = UserLibraryRepoSqlLite()

    def create_library(self, user_id):
        return self.repo.create_library(user_id)

    def list_ebooks(self, user_id):
        return self.repo.list_ebooks(user_id)

    def add_to_library(self, user_id, ebook_id):
        return self.repo.add_to_library(user_id, ebook_id)