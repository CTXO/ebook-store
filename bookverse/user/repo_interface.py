from abc import ABC, abstractmethod

class IUserRepo(ABC):
    @abstractmethod
    def create(self, name, email, password_hash):
        raise NotImplementedError

    @abstractmethod
    def update(self, user_id, name, email, password_hash):
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, user_id):
        raise NotImplementedError

    @abstractmethod
    def retrieve_by_email(self, email):
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id):
        raise NotImplementedError
