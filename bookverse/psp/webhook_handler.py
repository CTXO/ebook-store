import json

from flask import Blueprint
from flask import request

from .interface import IPSP
from .pspfacade import PSPFacade

webhook_handler = Blueprint('webhook_handler', __name__, url_prefix='/webhooks')


class WebhookHandler:
    def __init__(self):
        self.psp_facade = PSPFacade()

@webhook_handler.route('/', methods=['POST'])
def webhook():
    handler = WebhookHandler()
    webhook_data = handler.psp_facade.get_webhook_data(request)
    return handler.psp_facade.payment_succeeded(webhook_data)



