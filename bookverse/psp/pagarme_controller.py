import json

from pagarmecoreapi.exceptions.error_exception import ErrorException

from ..library.library_crud import LibraryCrud
from .interface import IPSP
from .pagarme_adapter import PagarmeAdapter
from ..helpers.payment_info import PaymentInfo


class PagarmeController(IPSP):
    def __init__(self):
        self.adapter = PagarmeAdapter()
        self.library_crud = LibraryCrud()

    def checkout(self, payment_info: PaymentInfo):
        try:
            orders_response = self.adapter.create_order(payment_info)
        except ErrorException as e:
            return {'success': False, 'message': e.message}
        return {'success': True, 'message': 'Pagamento efetuado com sucesso'}

    def get_webhook_data(self, webhook_request) -> dict:
        return json.loads(webhook_request.data)

    def payment_succeeded(self, webhook_data: dict):
        metadata = webhook_data.get('data').get('metadata')
        ebook_ids = json.loads(metadata.get('ebook_ids'))
        user_id = metadata.get('user_id')
        for ebook_id in ebook_ids:
            self.library_crud.add_to_library(user_id, ebook_id)
        return {'status': 'ok'}


