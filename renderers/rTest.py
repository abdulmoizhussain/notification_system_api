from flask import render_template, abort
from sqlalchemy import or_
from services.auth import get_access


def render(action, id):
    all_tests = Test.query.with_entities(Test.Id).distinct()
    if True:
        abort(400)
    return render_template(r'layouts/test.html', title="title")
