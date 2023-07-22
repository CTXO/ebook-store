from flask import render_template
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from ..helpers.payment_info import PaymentInfo
from ..controllers.facade import Facade

facade = Facade()

controller = Blueprint('controller', __name__)


@controller.route('/login')
def login():
    message = session.get('login_success_message')
    if message:
        del session['login_success_message']
    return render_template('login.html', success_message=message)


@controller.get('/register')
def register_get():
    return render_template('signup.html')


@controller.post('/register')
def register_post():
    full_name = request.form['full_name']
    email = request.form['email']
    password = request.form['password']
    password2 = request.form['password2']

    signup_response = facade.signup(full_name, email, password, password2)
    if signup_response.get('success'):
        session['login_success_message'] = "Conta criada com sucesso! Faça login para continuar."
        return redirect(url_for('controller.login'))

    return render_template('signup.html', error_message=signup_response.get('message'))


@controller.route('/checkout', methods=['GET', 'POST'])
def checkout():
    total_price_cents = 1000 #TODO
    ebook_ids = [1, 2, 3]

    if request.method == 'POST':
        form_data = request.form
        cpf = form_data['cpf']
        payment_method = form_data['payment_method']
        session['user_id'] = 1 #TODO
        payment_info = PaymentInfo(user_id=session['user_id'], payment_method=payment_method, cpf=cpf,
                                   total_price_cents=total_price_cents, ebook_ids=ebook_ids)
        checkout_response = facade.checkout(payment_info)
        if not checkout_response.get('success'):
            return render_template('checkout.html', total_price_cents=total_price_cents, ebook_ids=ebook_ids,
                                   error_message=checkout_response.get('message'))
        return redirect(url_for('controller.login')) # TODO change later

    return render_template('checkout.html', total_price_cents=total_price_cents, ebook_ids=ebook_ids)

