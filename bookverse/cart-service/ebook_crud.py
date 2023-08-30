from .repositories.ebook_repo_interface import IEbookRepo
from .repositories.ebook_repository import EbookRepoSqlLite


class EbookCrud:
    def __init__(self):
        self.repo: IEbookRepo = EbookRepoSqlLite()

    def list_available_ebooks(self, user_id):
        return self.repo.list_available_ebooks(user_id)
