from ..app import db

from .repo_interface import IEbookRepo


class EbookRepoSqlLite(IEbookRepo):
    def list_available_ebooks(self):
        raise NotImplementedError

    def add_to_cart(self):
        raise NotImplementedError

    def remove_from_cart(self):
        raise NotImplementedError
