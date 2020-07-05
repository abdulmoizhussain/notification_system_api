from flask_jwt_extended import create_access_token as _create_access_token, \
    create_refresh_token as _create_refresh_token
from passlib.apps import custom_app_context as _custom_app_context
from datetime import timedelta as _timedelta
import sqlalchemy as _sql
from application import db as _db
from common import AppRole as _AppRole


class User(_db.Model):
    __tablename__ = 'User'
    id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    Username = _sql.Column(_sql.String, nullable=False, unique=False)
    DisplayName = _sql.Column(_sql.String, nullable=False)
    PasswordHash = _sql.Column(_sql.String, nullable=False)
    UserRole = _sql.Column(_sql.Integer, nullable=False)
    RollNumber = _sql.Column(_sql.String, nullable=True)
    CmsId = _sql.Column(_sql.String, nullable=True)
    EnrollmentNumber = _sql.Column(_sql.String, nullable=True)
    Timestamp = _sql.Column(_sql.DateTime(timezone=True), index=True, default=_sql.func.now())

    def is_admin(self):
        return self.UserRole == _AppRole.Admin

    def create_password_hash(self, password):
        self.PasswordHash = _custom_app_context.encrypt(password)

    def generate_authorization_tokens(self, expiry_timedelta=6):
        expiry_timedelta = _timedelta(hours=expiry_timedelta)
        return {
            'access_token': _create_access_token(identity=self.id, expires_delta=expiry_timedelta),
            'refresh_token': _create_refresh_token(identity=self.id, expires_delta=expiry_timedelta)
        }

    def verify_password(self, password):
        return _custom_app_context.verify(password, self.PasswordHash)
