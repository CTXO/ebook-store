from abc import ABC
from abc import abstractmethod


class ICartRepo(ABC):
    @abstractmethod
    def create_cart(self, user_id):
        raise NotImplementedError

    @abstractmethod
    def list_ebooks(self, user_id):
        raise NotImplementedError

    @abstractmethod
    def add_to_cart(self, user_id, ebook_id):
        raise NotImplementedError
