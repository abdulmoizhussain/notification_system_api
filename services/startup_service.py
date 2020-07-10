import os as _os
from application import db as _db
from repository import user_repository as _user_repository, semester_repository as _semester_repository
from common.AppRole import AppRole as _AppRole


def initialize_default_values():
    if not _os.path.exists("db.sqlite"):
        _create_database()

    _add_default_admin_user()
    _add_semester_names()
    _add_week_days()
    _add_time_slots()


# noinspection PyUnresolvedReferences
def _create_database():
    from repository.models.User import User
    from repository.models.WeekDay import WeekDay
    from repository.models.TimeSlot import TimeSlot
    from repository.models.Teacher import Teacher
    from repository.models.Student import Student
    from repository.models.Semester import Semester
    from repository.models.Department import Department
    from repository.models.Course import Course
    from repository.models.ClassTimetable import ClassTimetable
    from repository.models.Event import Event
    from repository.models.Notification import Notification
    _db.create_all()
    _db.session.commit()


def _add_default_admin_user():
    admin_user = _user_repository.get_one_admin_by_username("admin")
    if admin_user is None:
        _user_repository.create_one(
            "admin",
            "admin",
            _AppRole.Admin,
        )


def _add_semester_names():
    s1 = _semester_repository.get_one_by_name('Semester 1')
    if not s1:
        _semester_repository.create_one('Semester 1')
    s2 = _semester_repository.get_one_by_name('Semester 2')
    if not s2:
        _semester_repository.create_one('Semester 2')
    s3 = _semester_repository.get_one_by_name('Semester 3')
    if not s3:
        _semester_repository.create_one('Semester 3')
    s4 = _semester_repository.get_one_by_name('Semester 4')
    if not s4:
        _semester_repository.create_one('Semester 4')
    s5 = _semester_repository.get_one_by_name('Semester 5')
    if not s5:
        _semester_repository.create_one('Semester 5')
    s6 = _semester_repository.get_one_by_name('Semester 6')
    if not s6:
        _semester_repository.create_one('Semester 6')
    s7 = _semester_repository.get_one_by_name('Semester 7')
    if not s7:
        _semester_repository.create_one('Semester 7')
    s8 = _semester_repository.get_one_by_name('Semester 8')
    if not s8:
        _semester_repository.create_one('Semester 8')


def _add_week_days():
    pass


def _add_time_slots():
    pass
