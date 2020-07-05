from flask import render_template as _render_template
from application import app as _app, Socket as _Socket
from services import startup_service as _startup_service


@_app.route("/")
@_app.route("/index")
@_app.route("/signin")
@_app.route("/login")
def sign_in():
    return _render_template(r'layouts/test.html', title="title")


# api endpoints
_app.add_url_rule("/api/user", "new_user", _startup_service, methods=["POST"])

# _app.add_url_rule("/api/test", "new_test", test_api, methods=["POST"])
# _app.add_url_rule("/tester", "new_tester", tester_function, defaults={"action": None, "id": None})
# _app.add_url_rule("/tester/<action>/", "new_tester", tester_function, defaults={"id": None})
# _app.add_url_rule("/tester/<action>/<id>", "new_tester", tester_function)

# if __name__ == "__main__":


_startup_service.initialize_default_values()
# app.run(debug=True, host="0.0.0.0", port=5000)
_Socket.io.run(_app, host="0.0.0.0", port=5000, debug=True, use_reloader=False)
