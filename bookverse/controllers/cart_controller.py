from ..cart.cart_crud import CartCrud


class CartController:
    cart_crud = CartCrud()

    def add_to_cart(self, user_id, ebook_id):
        try:
            cart = self.cart_crud.add_to_cart(user_id, ebook_id)
        except:
            return {'success': False, 'message': 'Erro ao adicionar ao carrinho'}
        return {'success': True, 'message': 'Carrinho adicionado com sucesso!'}

    def list_ebooks(self, user_id):
        ebooks = self.cart_crud.list_ebooks(user_id)
        return ebooks
