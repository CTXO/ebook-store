from flask import render_template
from flask import Flask
app = Flask(__name__)

from bookverse.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/login')
def test():
    return render_template('login.html')
