from abc import ABC, abstractmethod


class IEbookRepo(ABC):
    @abstractmethod
    def list_available_ebooks(self, user_id):
        raise NotImplementedError
