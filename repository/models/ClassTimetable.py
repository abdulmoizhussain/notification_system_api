import sqlalchemy as _sql
from application import db as _db


class ClassTimetable(_db.Model):
    """
    Composite Keys: DepartmentId + SemesterId + YearSpanName: <- must not be same for more than rows at a time.
    """
    __tablename__ = 'ClassTimetable'
    Id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    Name = _sql.Column(_sql.String, nullable=False, unique=True)
    DepartmentId = _sql.Column(_sql.Integer, _sql.ForeignKey('Department.Id'), nullable=False)
    SemesterId = _sql.Column(_sql.Integer, _sql.ForeignKey('Semester.Id'), nullable=False)
    YearSpanName = _sql.Column(_sql.String, nullable=False)
    Timestamp = _sql.Column(_sql.DateTime(timezone=True), index=True, default=_sql.func.now())
