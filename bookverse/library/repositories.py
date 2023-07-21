from .repo_interface import IUserLibraryRepo
from ..app import db

from .models import UserLibrary


class UserLibraryRepoSqlLite(IUserLibraryRepo):
    def create_library(self, user_id):
        library = UserLibrary(user_id)
        db.session.add(library)
        db.session.commit()
        return library

    def list_ebooks(self, user_id):
        library = UserLibrary.query.filter_by(user_id=user_id).first()
        if not library:
            raise Exception('Library not found')
        return library.ebooks
