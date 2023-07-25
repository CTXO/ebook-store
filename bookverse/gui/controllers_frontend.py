import json

from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for


from ..controllers.facade import Facade
from ..helpers.payment_info import PaymentInfo

facade = Facade()

controller = Blueprint('controller', __name__)


def requires_login(func):
    def wrapper():
        if 'userid' not in session:
            return redirect(url_for('controller.login'))
        return func()
    wrapper.__name__ = func.__name__
    return wrapper


@controller.route('/')
def home():
    return redirect(url_for('controller.login'))


@controller.get('/login')
def login():
    if session.get('userid'):
        return redirect(url_for('controller.ebooks'))
    return render_template('login.html')


@controller.get('/logout')
def logout():
    session.clear()
    return redirect(url_for('controller.login'))


@controller.post('/login')
def login_post():
    # login code goes here
    next_url = request.args.get('next')
    email = request.form['email']
    password = request.form['password']
    login_response = facade.login(email, password)
    if login_response.get('success'):
        session['login_success_message'] = "Login feito com sucesso"
        session['userid'] = login_response.get('user').id
        if next_url:
            return redirect(next_url)
        return redirect(url_for('controller.login'))
    return render_template('login.html', error_message=login_response.get('message'))


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


@controller.route('/ebooks')
@requires_login
def ebooks():
    ebooks_query = facade.list_available_ebooks(session.get('user_id'))
    return render_template('ebooks.html', ebooks=ebooks_query)


@controller.route('/checkout', methods=['GET', 'POST'])
@requires_login
def checkout():

    user_id = session['userid']
    ebooks_qs = facade.list_cart_ebooks(user_id)

    ebook_ids = [ebook.id for ebook in ebooks_qs]

    total_price_cents = 0
    for ebook in ebooks_qs:
        total_price_cents += ebook.price_cents

    total_price_parsed = f"R${total_price_cents / 100:.2f}".replace('.', ',')

    if request.method == 'POST':
        form_data = request.form
        payment_method = form_data['payment_method']
        payment_info = PaymentInfo(user_id=session['userid'], payment_method=payment_method,
                                   total_price_cents=total_price_cents, ebook_ids=ebook_ids)
        checkout_response = facade.checkout(payment_info)
        if not checkout_response.get('success'):
            return render_template('checkout.html', total_price_parsed=total_price_parsed,
                                   error_message=checkout_response.get('message'), ebooks=ebooks_qs)
        return redirect(url_for('controller.library'))

    return render_template('checkout.html', total_price_parsed=total_price_parsed, ebooks=ebooks_qs)


@controller.route('/library')
@requires_login
def library():
    user_id = session['userid']
    ebooks_qs = facade.list_library_ebooks(user_id)
    return render_template('library.html', ebooks=ebooks_qs)


@controller.post('/add-cart')
@requires_login
def add_cart():
    user_id = session['userid']
    post_data = json.loads(request.data.decode())
    add_response = facade.add_to_cart(user_id, int(post_data['ebook_id']))
    return add_response

