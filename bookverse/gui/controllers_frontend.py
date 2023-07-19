from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

from ..controllers.facade import Facade
from ..database import db_session

app = Flask(__name__)


facade = Facade()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        signup_response = facade.signup(full_name, email, password, password2)
        if signup_response.get('success'):
            return render_template('login.html', success="success")
        return render_template('signup.html', message=signup_response.get('message'))

    return render_template('signup.html')
