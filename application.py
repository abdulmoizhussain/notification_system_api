from flask import Flask as _Flask
from flask_marshmallow import Marshmallow as _Marshmallow
from flask_jwt_extended import JWTManager as _JWTManager
from datetime import timedelta as _timedelta
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from flask_socketio import SocketIO as _SocketIO

_access_token_expiry = _timedelta(hours=6)
_refresh_token_expiry = _timedelta(hours=12)

# https://stackoverflow.com/a/42791810/8075004
app = _Flask(
    __name__,
    static_url_path='',
    static_folder='templates',
    template_folder='templates'
)

app.secret_key = "application-secret-key"
app.config['JWT_SECRET_KEY'] = "application-secure-key"
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = _access_token_expiry
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = _refresh_token_expiry
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

ma = _Marshmallow(app)
jwt = _JWTManager(app)
db = _SQLAlchemy(app)


class Socket:
    io = _SocketIO(app)
