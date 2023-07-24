from abc import ABC, abstractmethod


class IUserLibraryRepo(ABC):
    @abstractmethod
    def create_library(self, user_id):
        raise NotImplementedError

    @abstractmethod
    def list_ebooks(self, user_id):
        raise NotImplementedError

    @abstractmethod
    def add_to_library(self, user_id, ebook_id):
        raise NotImplementedError
