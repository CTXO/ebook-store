from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/login')
def test():
    return render_template('login.html')
