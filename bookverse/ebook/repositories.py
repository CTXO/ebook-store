from .repo_interface import IEBookRepo
from ..app import db

from .models import Ebook


class EbookRepoSqlLite(IEBookRepo):
    def list_available_ebooks(self, title, pages, authors, year_of_release, price):
        return super().list_available_ebooks(title, pages, authors, year_of_release, price)
    
    def add_to_cart(self, user_id, title, price):
        return super().add_to_cart(user_id, title, price)
    
    def remove_from_cart(self, user_id, title):
        return super().remove_from_cart(user_id, title)
    
    def add_to_library(self, user_id, title):
        return super().add_to_library(user_id, title)
    