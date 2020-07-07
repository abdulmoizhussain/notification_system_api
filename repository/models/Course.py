import sqlalchemy as _sql
from application import db as _db


class Course(_db.Model):
    __tablename__ = 'Course'
    Id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    TeacherId = _sql.Column(_sql.Integer, _sql.ForeignKey('Teacher.Id'), nullable=False, unique=True)
    DepartmentId = _sql.Column(_sql.Integer, _sql.ForeignKey('Department.Id'), nullable=False)
    Name = _sql.Column(_sql.String, nullable=False, unique=True)
    CreditHours = _sql.Column(_sql.Integer, nullable=False)
    Fee = _sql.Column(_sql.Integer, nullable=False)
    Timestamp = _sql.Column(_sql.DateTime(timezone=True), index=True, default=_sql.func.now())
