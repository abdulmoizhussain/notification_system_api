import sqlalchemy as _sql
from application import db as _db


class Teacher(_db.Model):
    __tablename__ = 'Teacher'
    Id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    UserId = _sql.Column(_sql.Integer, _sql.ForeignKey('User.Id'), nullable=False, unique=True)
    Name = _sql.Column(_sql.String, nullable=False)
    Title = _sql.Column(_sql.String, nullable=False)
    Email = _sql.Column(_sql.String, nullable=False, unique=True)
    Gender = _sql.Column(_sql.Integer, nullable=False)
    Timestamp = _sql.Column(_sql.DateTime(timezone=True), index=True, default=_sql.func.now())
