from ..ebook_crud import EbookCrud


class EbookController:
    ebook_crud = EbookCrud()

    def list_available_ebooks(self, user_id):
        return self.ebook_crud.list_available_ebooks(user_id)

    