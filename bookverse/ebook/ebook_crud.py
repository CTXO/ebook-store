from .repositories import EbookRepoSqlLite
from .repo_interface import IEbookRepo
from .repositories import EbookRepoSqlLite


class EbookCrud:
    def __init__(self):
        self.repo: IEbookRepo = EbookRepoSqlLite()

    def list_available_ebooks(self, user_id):
        return self.repo.list_available_ebooks(user_id)
