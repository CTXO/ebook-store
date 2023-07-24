from abc import ABC, abstractmethod


class IEBookRepo(ABC):
    @abstractmethod
    def list_available_ebooks(self, title, pages, authors, year_of_release, price):
        raise NotImplementedError


    def add_to_cart(self, cart_id, library_id, title, price):
        raise NotImplementedError
    
    
    def remove_from_cart(self, cart_id, library_id title):
        raise NotImplementedError
    
    
    def add_to_library(self, cart_id, library_id,  title):
        raise NotImplementedError