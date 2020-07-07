from flask import \
    request, jsonify as _jsonify, g as _local_proxy
# session,\
from repository.models.User import User as _User
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity
from flask_httpauth import HTTPBasicAuth
from common.methods import props_required, wraps
from common.AppRole import AppRole as _AppRole
from repository import user_repository as _user_repository

auth = HTTPBasicAuth()


# def get_access():
#     return session[KEYS.TEST_ACCESS_LEVEL] if KEYS.TEST_ACCESS_LEVEL in session else ACCESS.Default


@props_required("username:str", "password:str", "user_roll:int")
def login():
    username: str = request.json.get('username')
    password: str = request.json.get('password')
    user_roll: int = request.json.get('user_roll')

    if not _AppRole.is_valid(user_roll):
        return _jsonify({"msg": "user_roll does not exists."}), 400

    user = _user_repository.get_one_by_username(username)

    if not user or not user.verify_password(password):
        return _jsonify({"msg": "Invalid credentials."}), 401

    # session[KEYS.TEST_ACCESS_LEVEL] = user.UserRole
    token_response = user.generate_authorization_tokens()
    return token_response


@auth.verify_password
def verify_password(testname_or_token, password):
    user = _User.query.filter(testname=testname_or_token).first()
    if not user or not user.verify_password(password):
        return False
    _local_proxy.user = user
    return True


@auth.login_required
def get_auth_token():
    token = _local_proxy.user.generate_authorization_tokens()
    return _jsonify(token)


@jwt_refresh_token_required
def refresh_token():
    user = _User.query.get(get_jwt_identity())
    token_object = user.generate_authorization_tokens()
    return _jsonify(token_object)


def required_app_role(*access_levels):
    def inner_function(function):
        @wraps(function)
        def wrapper():
            authorized = False
            test = _User.query.get(get_jwt_identity())
            for access_level in access_levels:
                if access_level == test.UserRole:
                    authorized = True
                    break
            if not authorized:
                return _jsonify({"msg": "Test %s is unauthorized." % test.testname}), 401
            return function()

        return wrapper

    return inner_function
