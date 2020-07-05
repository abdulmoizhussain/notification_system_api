from flask import session, request, jsonify, g
from repository.models.User import User as _User
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity
from flask_httpauth import HTTPBasicAuth
from common.methods import props_required, wraps
from common import AppRole as _AppRole

auth = HTTPBasicAuth()


def get_access():
    return session[KEYS.TEST_ACCESS_LEVEL] if KEYS.TEST_ACCESS_LEVEL in session else ACCESS.Default


@props_required("testname", "password")
def login():
    testname = request.json.get('testname')
    password = request.json.get('password')
    try:
        test = _User.query.filter_by(testname=testname).first()
        verify = test.verify_password(password)
        if verify:
            token_response = test.generate_authorization_tokens(6)
            session[KEYS.TEST_ACCESS_LEVEL] = test.UserRole
        else:
            raise Exception("%s not verified !" % testname)
        return token_response
    except Exception as e:
        return jsonify({"status": "failed", "Comment": str(e)})


@auth.verify_password
def verify_password(testname_or_token, password):
    test = _User.query.filter(testname=testname_or_token).first()
    if not test or not test.verify_password(password):
        return False
    g.test = test
    return True


@auth.login_required
def get_auth_token():
    token = g.test.generate_authorization_tokens(6)
    return token


@jwt_refresh_token_required
def refresh_token():
    user = _User.query.get(get_jwt_identity())
    token_object = user.generate_authorization_tokens(6)
    return jsonify(token_object)


def required_app_role(*access_levels_args):
    def inner_function(function):
        @wraps(function)
        def wrapper():
            authorized = False
            test = _User.query.get(get_jwt_identity())
            for access_level in access_levels_args:
                if access_level == test.UserRole:
                    authorized = True
                    break
            if not authorized:
                return jsonify({"msg": "Test %s is unauthorized." % test.testname}), 401
            return function()

        return wrapper

    return inner_function
