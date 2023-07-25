from ..library.library_crud import LibraryCrud


class LibraryController:
    def __init__(self):
        self.library_crud = LibraryCrud()

    def list_library_ebooks(self, user_id):
        return self.library_crud.list_ebooks(user_id)
