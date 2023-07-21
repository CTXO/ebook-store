from abc import ABC, abstractmethod


class IUserLibraryRepo(ABC):
    @abstractmethod
    def create_library(self, user_id):
        raise NotImplementedError

    @abstractmethod
    def list_ebooks(self, user_id):
        raise NotImplementedError
