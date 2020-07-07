from flask_jwt_extended import create_access_token, create_refresh_token
from passlib.apps import custom_app_context as pwd_con
from application import db
from datetime import datetime as _datetime


class Tests(db.Model):
    __tablename__ = 'Test'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Test = db.Column(db.String(25))
    Test2 = db.Column(db.Integer, db.ForeignKey('Test1.id'), nullable=True)
    Test3 = db.Column(db.Integer, db.ForeignKey('Test2.id'), unique=True)
    Time_Stamp = db.Column(db.DateTime, index=True, default=_datetime.now)
    Access = db.Column(db.Integer)

    def verify_password(self, password):
        return pwd_con.verify(password, self.password_hash)
