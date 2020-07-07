import sqlalchemy as _sql
from application import db as _db


class Semester(_db.Model):
    __tablename__ = 'Semester'
    Id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    Name = _sql.Column(_sql.String, nullable=False, unique=True)
