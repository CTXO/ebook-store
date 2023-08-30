import json

from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for


from ..controllers.facade import Facade

facade = Facade()

controller = Blueprint('controller', __name__)

@controller.route('/loginnn')
def login():
    return 'hello login'

@controller.route('/ebooks')
def ebooks():
    userid = request.args.get('userid')
    if userid:
        session['userid'] = userid
    ebooks_query = facade.list_available_ebooks(session.get('user_id'))
    return render_template('ebooks.html', ebooks=ebooks_query)


@controller.route('/checkout', methods=['GET', 'POST'])
def checkout():
    user_id = session.get('user_id')
    ebooks_qs = facade.list_cart_ebooks(user_id)

    total_price_cents = 0
    for ebook in ebooks_qs:
        total_price_cents += ebook.price_cents

    total_price_parsed = f"R${total_price_cents / 100:.2f}".replace('.', ',')

    return render_template('checkout.html', total_price_parsed=total_price_parsed, ebooks=ebooks_qs)


@controller.post('/add-cart')
def add_cart():
    user_id = session.get('userid')
    post_data = json.loads(request.data.decode())
    add_response = facade.add_to_cart(user_id, int(post_data['ebook_id']))
    return add_response
