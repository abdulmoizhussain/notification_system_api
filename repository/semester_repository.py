from repository.models.Semester import Semester as _Semester
from application import db as _db


def get_one_by_name(semester_name: str) -> _Semester:
    return _Semester.query.filter(_Semester.Name == semester_name).first()


def create_one(semester_name: str):
    semester = _Semester()

    semester.Name = semester_name

    _db.session.add(semester)
    _db.session.commit()
