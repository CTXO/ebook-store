import json
from typing import TypedDict

from pagarmecoreapi.models.create_order_request import CreateOrderRequest
from pagarmecoreapi.models.create_order_item_request import CreateOrderItemRequest
from pagarmecoreapi.models.get_order_response import GetOrderResponse
from pagarmecoreapi.models.create_payment_request import CreatePaymentRequest
from pagarmecoreapi.models.create_pix_payment_request import CreatePixPaymentRequest
from pagarmecoreapi.exceptions.error_exception import ErrorException
from pagarmecoreapi.models.create_boleto_payment_request import CreateBoletoPaymentRequest
from pagarmecoreapi.pagarmecoreapi_client import PagarmecoreapiClient

from .pagarme_adapter import PagarmeAdapter
from ..helpers.payment_info import PaymentInfo


class CheckoutResponse(TypedDict):
    success: bool
    message: str


class PagarmeController:
    def __init__(self):
        self.adapter = PagarmeAdapter()

    def checkout(self, payment_info: PaymentInfo):
        try:
            orders_response = self.adapter.create_order(payment_info)
        except ErrorException as e:
            return {'success': False, 'message': e.message}
        return {'success': True, 'message': 'Pagamento efetuado com sucesso'}

    def payment_succeeded(self, user_id: int, ebook_ids: list[int]):
        print(f'{user_id=}')
        print(f'{ebook_ids=}')
        pass

