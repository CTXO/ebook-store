from abc import ABC, abstractmethod


class ICartRepo(ABC):
    @abstractmethod
    def create_cart(self, user_id):
        raise NotImplementedError

    @abstractmethod
    def list_ebooks(self, user_id):
        raise NotImplementedError


