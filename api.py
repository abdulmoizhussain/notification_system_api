import os as _os
from flask import render_template as _render_template, Response as _Response
from application import app as _app, Socket as _Socket
from services import startup_service as _startup_service
# https://stackoverflow.com/a/21755201/8075004
from mimetypes import guess_type as _guess_mime_type


@_app.route("/")
@_app.route("/index")
@_app.route("/signin")
@_app.route("/login")
def sign_in():
    # pass
    return _render_template(r'base.html', title="title")
    # return _render_template(r'layouts/test.html', title="title")


# api endpoints
# _app.add_url_rule("/api/user", "new_user", _startup_service, methods=["POST"])

# _app.add_url_rule("/api/test", "new_test", test_api, methods=["POST"])
# _app.add_url_rule("/tester", "new_tester", tester_function, defaults={"action": None, "id": None})
# _app.add_url_rule("/tester/<action>/", "new_tester", tester_function, defaults={"id": None})
# _app.add_url_rule("/tester/<action>/<id>", "new_tester", tester_function)


# https://stackoverflow.com/q/20646822/8075004
def get_file(src):
    try:
        return open(src).read()
    except IOError:
        return None


def root_dir():
    return _os.path.abspath(_os.path.dirname(__file__))


_root_directory_path = root_dir()


@_app.route('/static/<path:path>')
def tester(path):
    file_path = _os.path.join(_root_directory_path, 'templates/static', path).replace('\\', '/')
    # https://stackoverflow.com/a/541394/8075004
    file_extension = (_os.path.splitext(file_path)[1] or '').lower()
    file_to_send = get_file(file_path)
    if file_to_send is None:
        return 'File not found'
    if file_extension == '.js':
        return _Response(file_to_send, mimetype='application/javascript')
    # https://stackoverflow.com/a/11774026/8075004
    return _Response(file_to_send, mimetype=_guess_mime_type(file_path)[0])


if __name__ == "__main__":
    _startup_service.initialize_default_values()
    # _app.run(debug=True, host="0.0.0.0", port=5000)
    _Socket.io.run(_app, host="0.0.0.0", port=5000, debug=True, use_reloader=False)
