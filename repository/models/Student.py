import sqlalchemy as _sql
from application import db as _db


class Student(_db.Model):
    __tablename__ = 'Student'
    Id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    UserId = _sql.Column(_sql.Integer, _sql.ForeignKey('User.Id'), nullable=False, unique=True)
    DepartmentId = _sql.Column(_sql.Integer, _sql.ForeignKey('Department.Id'), nullable=False)
    Name = _sql.Column(_sql.String, nullable=False)
    RollNumber = _sql.Column(_sql.String, nullable=True, unique=True)
    CmsId = _sql.Column(_sql.String, nullable=True, unique=True)
    EnrollmentNumber = _sql.Column(_sql.String, nullable=True, unique=True)
    Gender = _sql.Column(_sql.Integer, nullable=False)
    Timestamp = _sql.Column(_sql.DateTime(timezone=True), index=True, default=_sql.func.now())
