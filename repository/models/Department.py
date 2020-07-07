import sqlalchemy as _sql
from application import db as _db


class Department(_db.Model):
    __tablename__ = 'Department'
    Id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    Name = _sql.Column(_sql.String, nullable=False, unique=True)
    Timestamp = _sql.Column(_sql.DateTime(timezone=True), index=True, default=_sql.func.now())
