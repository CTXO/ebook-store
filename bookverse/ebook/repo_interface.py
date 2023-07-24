from abc import ABC, abstractmethod


class IEbookRepo(ABC):
    @abstractmethod
    def list_available_ebooks(self):
        raise NotImplementedError

    @abstractmethod
    def add_to_cart(self):
        raise NotImplementedError

    @abstractmethod
    def remove_from_cart(self):
        raise NotImplementedError
