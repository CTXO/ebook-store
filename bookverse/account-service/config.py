import os
basedir = os.path.abspath(os.path.dirname(__file__))
configs = {
    "SQLALCHEMY_DATABASE_URI": f"sqlite:///{os.path.join(basedir, 'account.db')}",
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    "PAGARME_API_KEY": "sk_test_PxeyJpoUVfQrVGYD",
}