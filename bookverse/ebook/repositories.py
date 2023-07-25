from ..app import db
from .models import Ebook

from .repo_interface import IEbookRepo


class EbookRepoSqlLite(IEbookRepo):
    def list_available_ebooks(self, user_id):
        ebooks = Ebook.query.all()
        return ebooks
