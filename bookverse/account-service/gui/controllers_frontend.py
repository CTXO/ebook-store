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
