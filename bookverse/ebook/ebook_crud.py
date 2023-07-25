<<<<<<< HEAD
from .repositories import EbookRepoSqlLite

class EbookCrud:
    def __init__(self):
        self.repo = EbookRepoSqlLite()

    def list_available_ebooks(self, title, pages, authors, year_of_release, price):


    def add_to_cart(self, cart_id, library_id, title, price):


    def remove_from_cart(self, cart_id, library_id, title):

    
    def add_to_library(self, cart_id, library_id, title):
=======
from .repo_interface import IEbookRepo
from .repositories import EbookRepoSqlLite


class EbookCrud:
    def __init__(self):
        self.repo: IEbookRepo = EbookRepoSqlLite()

    def list_available_ebooks(self):
        self.repo.list_available_ebooks()

    def add_to_cart(self):
        self.repo.add_to_cart()

    def remove_from_cart(self):
        self.repo.remove_from_cart()
>>>>>>> upstream/master
