from flask_jwt_extended import create_access_token, create_refresh_token
from passlib.apps import custom_app_context as pwd_con
from repository.database import db
from datetime import datetime as _datetime


class Tests(db.Model):
    __tablename__ = 'Test'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Test = db.Column(db.String(25))
    Test2 = db.Column(db.Integer, db.ForeignKey('Test1.id'), nullable=True)
    Test3 = db.Column(db.Integer, db.ForeignKey('Test2.id'), unique=True)
    Time_Stamp = db.Column(db.DateTime, index=True, default=_datetime.now)
    Access = db.Column(db.Integer)

    def is_admin(self):
        return self.Access == ACCESS.Admin

    def hash_password(self, password):
        self.password_hash = pwd_con.encrypt(password)

    def generate_auth_token(self, expiration=6):
        expiration = datetime.timedelta(hours=expiration)
        ret = {'token': create_access_token(identity=self.id, expires_delta=expiration),
               'refresh': create_refresh_token(identity=self.id, expires_delta=expiration)}
        return jsonify(ret)

    def verify_password(self, password):
        return pwd_con.verify(password, self.password_hash)
