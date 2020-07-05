from repository.models.User import User as _User
from common import AppRole as _AppRole
import sqlalchemy as _sqlalchemy
from application import db as _db


def get_one_admin_by_username(username: str):
    return _User.query.filter(_sqlalchemy.and_(
        _User.Username == username,
        _User.UserRole == _AppRole.Admin
    )).first()


def create_one(
        username: str,
        password: str,
        display_name: str,
        user_role: int,
        roll_number: str or None,
        cms_id: str or None,
        enrollment_number: str or None,
):
    new_user = _User()

    new_user.Username = username
    new_user.DisplayName = display_name
    new_user.UserRole = user_role
    new_user.RollNumber = roll_number
    new_user.CmsId = cms_id
    new_user.EnrollmentNumber = enrollment_number
    new_user.create_password_hash(password)

    _db.session.add(new_user)
    _db.session.commit()
