import json


from pagarmecoreapi.models.create_order_request import CreateOrderRequest
from pagarmecoreapi.models.get_order_response import GetOrderResponse
from pagarmecoreapi.models.create_order_item_request import CreateOrderItemRequest
from pagarmecoreapi.models.create_payment_request import CreatePaymentRequest
from pagarmecoreapi.models.create_pix_payment_request import CreatePixPaymentRequest
from pagarmecoreapi.models.create_boleto_payment_request import CreateBoletoPaymentRequest
from pagarmecoreapi.pagarmecoreapi_client import PagarmecoreapiClient

from ..config import configs
from ..helpers.payment_info import PaymentInfo


class PagarmeAdapter:
    def __init__(self):
        self.pagarme_api_key = configs.get('PAGARME_API_KEY')
        self.client = PagarmecoreapiClient(self.pagarme_api_key, '')

    def create_order(self, payment_info: PaymentInfo) -> GetOrderResponse:
        orders_controller = self.client.orders

        base_customer_id = 'cus_rVJOA9VI4I78B6nj'
        payment_method = payment_info.payment_method
        if payment_method == 'bank_slip':
            payment_method_parsed = 'boleto'
            payment_request = CreatePaymentRequest(
                payment_method=payment_method_parsed,
                boleto=CreateBoletoPaymentRequest(
                    bank='001'
                )
            )
        elif payment_method == 'pix':
            payment_method_parsed = 'pix'

            payment_request = CreatePaymentRequest(
                payment_method=payment_method_parsed,
                pix=CreatePixPaymentRequest(
                    expires_in=3600,
                )
            )
        else:
            return {'success': False, 'message': 'Método de pagamento inválido'}

        body = CreateOrderRequest(
            items=[
                CreateOrderItemRequest(
                    amount=int(payment_info.total_price_cents),
                    description='description',
                    quantity=1,
                )
            ],
            customer_id=base_customer_id,
            payments=[payment_request],
            code=f'{payment_info.user_id}-{str(payment_info.ebook_ids)}',
            metadata={
                'ebook_ids': json.dumps(payment_info.ebook_ids),
                'user_id': payment_info.user_id,
            }
        )
        return orders_controller.create_order(body=body)







