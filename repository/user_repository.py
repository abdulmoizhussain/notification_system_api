from repository.models.User import User as _User
from common.AppRole import AppRole as _AppRole
import sqlalchemy as _sqlalchemy
from application import db as _db


def get_one_admin_by_username(username: str) -> _User:
    return _User.query.filter(_sqlalchemy.and_(
        _User.Username == username,
        _User.UserRole == _AppRole.Admin
    )).first()


def get_one_by_username(username: str) -> _User:
    return _User.query.filter(_User.Username == username).first()


def create_one(
        username: str,
        password: str,
        user_role: int,
):
    new_user = _User()

    new_user.Username = username
    new_user.UserRole = user_role
    new_user.create_password_hash(password)

    _db.session.add(new_user)
    _db.session.commit()
