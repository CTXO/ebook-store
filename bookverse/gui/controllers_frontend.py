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
    return wrapper

@controller.get('/login')
def login():
    return render_template('login.html')

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


@controller.route('/checkout', methods=['GET', 'POST'])
@requires_login
def checkout():
    total_price_cents = 1000  # TODO
    ebook_ids = [1, 2, 3]

    if request.method == 'POST':
        form_data = request.form
        payment_method = form_data['payment_method']
        session['user_id'] = 1  # TODO
        payment_info = PaymentInfo(user_id=session['user_id'], payment_method=payment_method,
                                   total_price_cents=total_price_cents, ebook_ids=ebook_ids)
        checkout_response = facade.checkout(payment_info)
        if not checkout_response.get('success'):
            return render_template('checkout.html', total_price_cents=total_price_cents, ebook_ids=ebook_ids,
                                   error_message=checkout_response.get('message'))
        return redirect(url_for('controller.login'))  # TODO change later

    return render_template('checkout.html', total_price_cents=total_price_cents, ebook_ids=ebook_ids)


@controller.route('/library')
def library():
    session['user_id'] = 1  # TODO
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('controller.login')) # next= request.url
    ebooks = facade.list_ebooks(user_id)
    return render_template('library.html', ebooks=ebooks)
