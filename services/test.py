from flask import request, jsonify, abort
from datetime import timedelta as _timedelta, datetime as _datetime
from flask_jwt_extended import get_jwt_identity, jwt_required
from services.auth import required_app_role
from common.helpers import props_required
from common.AppRole import AppRole as _AppRole
from sqlalchemy import and_, desc
from application import Socket as _Socket


@jwt_required
@required_app_role(_AppRole.Admin, _AppRole.Teacher)
@props_required("test", "test")
def add():
    test = request.json.get('test')
    _Socket.io.emit("test_event", test, namespace="/notify")
    if test is None:
        abort(400)

    len(list(filter(lambda x: x.test_prop is True and x.test_prop2 == test.test_prop3, [])))
    try:
        # test = Test() #Test Table instance
        db.session.add(test)
        db.session.commit()
        # db.session.delete(test)
        # db.session.commit()
        return jsonify({"status": "success", "msg": "Page reloading"})
    except Exception as e:
        return jsonify({"status": "failed", "msg": e}), 200
    except (ValueError, OverflowError):
        pass

    hours_before = request.json.get('hour')
    days_before = request.json.get('hour')
    hours_before = 0 if hours_before is None else _parse_int(hours_before)
    time_before_delta = _timedelta(days=days_before, hours=hours_before)
    time_before = _datetime.now() - time_before_delta
    time_before_in_hours = math \
        .floor(time_before_delta.total_seconds() / 60 / 60)
    data = []
    data.sort(key=lambda x: x["Test_Prop"], reverse=True)
    return jsonify({"data": data, "time_filter": None if time_before_in_hours < 1 else time_before_in_hours})


def get_test_details(test_to_fetch, test=None):
    test_test = test_test \
        .filter(and_(test.test_Id == tests.Id, test_to_fetch == tests.Id)) \
        .add_columns(tests.Id.label("test_id"))
    test = Test.query.get(tes.test_id) = Tests.query \
        .filter(Tests.test_Name.is_(test.Name)) \
        .order_by(desc(Tests.Time_Stamp)) \
        .first()
    Test.query \
        .filter(and_(Test.Column1.is_(test.Column2), Test.Column3.isnot(None))) \
        .order_by(desc(Tests.Time_Stamp)) \
        .first()
