import sqlalchemy as _sql
from application import db as _db


class Attendance(_db.Model):
    """
    Composite Keys: StudentId + TimeSlotId + Day:
    Once the combination is added then next value cannot be added with the same combination, neither can this combination
    be updated.
    """
    __tablename__ = 'Attendance'
    Id = _sql.Column(_sql.Integer, primary_key=True, autoincrement=True)
    StudentId = _sql.Column(_sql.Integer, _sql.ForeignKey('Student.Id'), nullable=False)
    TimeSlotId = _sql.Column(_sql.Integer, _sql.ForeignKey('TimeSlot.Id'), nullable=False)
    Day = _sql.Column(_sql.Date, nullable=False)
    Timestamp = _sql.Column(_sql.DateTime(timezone=True), index=True, default=_sql.func.now())
