from .repositories import CartRepoSqlLite


class CartCrud:
    def __init__(self):
        self.repo = CartRepoSqlLite()

    def create_cart(self, user_id):
        return self.repo.create_cart(user_id)

    def list_ebooks(self, user_id):
        return self.repo.list_ebooks(user_id)

    def add_to_cart(self, user_id, ebook_id):
        return self.repo.add_to_cart(user_id, ebook_id)
