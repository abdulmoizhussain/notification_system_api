import sqlalchemy as _sql
from application import db as _db


class Event(_db.Model):
    __tablename__ = 'Event'
    Id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    Name = _sql.Column(_sql.String, nullable=False)
    Description = _sql.Column(_sql.String, nullable=False)
    ImageBase64 = _sql.Column(_sql.String, nullable=True)
    EventDate = _sql.Column(_sql.DateTime, nullable=False)
    EventFor = _sql.Column(_sql.Integer, nullable=False)
    StudentId = _sql.Column(_sql.Integer, _sql.ForeignKey('Student.Id'))
    DepartmentId = _sql.Column(_sql.Integer, _sql.ForeignKey('Department.Id'))
    Timestamp = _sql.Column(_sql.DateTime(timezone=True), index=True, default=_sql.func.now())
