from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

from ..database import db_session

app = Flask(__name__)


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

        return render_template('signup.html', success="success")
    return render_template('signup.html')
