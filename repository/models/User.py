from flask_jwt_extended import create_access_token as _create_access_token, \
    create_refresh_token as _create_refresh_token
from passlib.apps import custom_app_context as _custom_app_context
import sqlalchemy as _sql
from application import db as _db, app
from common.AppRole import AppRole as _AppRole


class User(_db.Model):
    __tablename__ = 'User'
    Id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    Username = _sql.Column(_sql.String, nullable=False, unique=False)
    PasswordHash = _sql.Column(_sql.String, nullable=False)
    UserRole = _sql.Column(_sql.Integer, nullable=False)
    Timestamp = _sql.Column(_sql.DateTime(timezone=True), index=True, default=_sql.func.now())

    def create_password_hash(self, password):
        self.PasswordHash = _custom_app_context.encrypt(password)

    def verify_password(self, password):
        return _custom_app_context.verify(password, self.PasswordHash)

    def is_admin(self):
        return self.UserRole == _AppRole.Admin

    def generate_authorization_tokens(self, expiry_timedelta=6):
        return {
            'access_token': _create_access_token(
                identity=self.Id,
                expires_delta=app.config["JWT_ACCESS_TOKEN_EXPIRES"]
            ),
            'refresh_token': _create_refresh_token(
                identity=self.Id,
                expires_delta=app.config["JWT_REFRESH_TOKEN_EXPIRES"]
            )
        }
