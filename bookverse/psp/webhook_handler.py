import json

from flask import Blueprint
from flask import request

from .pspfacade import PSPFacade

webhook_handler = Blueprint('webhook_handler', __name__, url_prefix='/webhooks')


@webhook_handler.route('/pagarme', methods=['POST'])
def pagarme_webhook_handler():
    data = json.loads(request.data)
    metadata = data.get('data').get('metadata')
    ebook_ids = json.loads(metadata.get('ebook_ids'))
    user_id = metadata.get('user_id')
    PSPFacade().payment_succeeded(int(user_id), ebook_ids)

    return {'status': 'ok'}

