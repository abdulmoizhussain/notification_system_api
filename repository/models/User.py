from flask_jwt_extended import create_access_token, create_refresh_token
from passlib.apps import custom_app_context as _custom_app_context
from datetime import datetime as _datetime, timedelta as _timedelta
from flask import jsonify as _jsonify
import sqlalchemy as _sql
from flask_sqlalchemy import Model
from common import AppRole as _AppRole


class Tests(_sql):
    __tablename__ = 'User'
    id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    Username = _sql.Column(_sql.String, nullable=False, unique=True)
    DisplayName = _sql.Column(_sql.String, nullable=False)
    PasswordHash = _sql.Column(_sql.String, nullable=False)
    UserRole = _sql.Column(_sql.Integer, _sql.ForeignKey(''), nullable=False)
    TimeStamp = _sql.Column(_sql.DateTime, index=True, default=_datetime.now)

    def is_admin(self):
        return self.UserRole == _AppRole.ADMIN

    def create_password_hash(self, password):
        self.PasswordHash = _custom_app_context.encrypt(password)

    def generate_authorization_tokens(self, expiry_timedelta=6):
        expiry_timedelta = _timedelta(hours=expiry_timedelta)
        response = {
            'token': create_access_token(identity=self.id, expires_delta=expiry_timedelta),
            'refresh': create_refresh_token(identity=self.id, expires_delta=expiry_timedelta)
        }
        return _jsonify(response)

    def verify_password(self, password):
        return _custom_app_context.verify(password, self.password_hash)
