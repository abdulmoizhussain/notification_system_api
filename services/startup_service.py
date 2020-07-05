import os as _os
from application import db as _db
from repository import user_repository as _user_repository
from common import AppRole as _AppRole


def initialize_default_values():
    from repository.models.User import User
    if not _os.path.exists("db.sqlite"):
        # noinspection PyUnresolvedReferences
        _db.create_all()
        _db.session.commit()

    admin_user = _user_repository.get_one_admin_by_username("admin")
    if admin_user is None:
        _user_repository.create_one(
            "admin",
            "admin",
            "Admin",
            _AppRole.Admin,
            None,
            None,
            None,
        )
    del admin_user
