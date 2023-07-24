from .repo_interface import IUserLibraryRepo
from ..app import db

from ..ebook.models import Ebook
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

    def add_to_library(self, user_id, ebook_id):
        library = UserLibrary.query.filter_by(user_id=user_id).first()
        ebook = Ebook.query.filter_by(id=ebook_id).first()
        if UserLibrary.query.filter(UserLibrary.ebooks.any(id=ebook_id)).first():
            return library
        if not library:
            raise Exception('Library not found')
        library.ebooks.append(ebook)
        db.session.commit()
        return library
