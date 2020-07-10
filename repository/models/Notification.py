import sqlalchemy as _sql
from application import db as _db


class Notification(_db.Model):
    __tablename__ = 'Notification'
    Id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    From = _sql.Column(_sql.Integer, nullable=False)
    SenderName = _sql.Column(_sql.String, nullable=False)
    Title = _sql.Column(_sql.String, nullable=False)
    Description = _sql.Column(_sql.String, nullable=False)
    NotificationFor = _sql.Column(_sql.Integer, nullable=False)
    StudentId = _sql.Column(_sql.Integer, _sql.ForeignKey('Student.Id'))
    DepartmentId = _sql.Column(_sql.Integer, _sql.ForeignKey('Department.Id'))
    Timestamp = _sql.Column(_sql.DateTime(timezone=True), index=True, default=_sql.func.now())
