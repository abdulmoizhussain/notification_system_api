# PLACE ONLY STATIC/INDEPENDENT Classes/Functions... here !

from flask import request as _request, jsonify as _jsonify
from functools import wraps as _wraps

_data_type = {
    "str": str,
    "int": int,
    "bool": bool,
    "dict": dict,
    "list": list,
    "float": float
}


def props_required(*json_props):
    def inner_function(function):
        @_wraps(function)
        def wrapper():
            content_type: str = _request.headers.get("Content-Type")
            if not content_type or type(content_type) is not str or "application/json" not in content_type.lower().strip():
                return _jsonify({"msg": "Missing request header: 'Content-Type': 'application/json; charset=utf-8'"}), 400
            del content_type
            m_props = ""  # missing props
            for arg in json_props:
                index = arg.find(":")
                # name = arg[:index] if index > -1 else arg
                if index > -1:
                    name = arg[:index]
                    type_name = arg[index:]
                    type_name = type_name[1:] if len(type_name) > 1 else "str"
                else:
                    name = arg
                    type_name = "str"
                # type_name = arg[index:]
                # type_name = type_name[1:] if len(type_name) > 1 else type_name
                # type_name = arg[index + 1:] if index > -1 else "str"
                prop = _request.json.get(name)
                if prop is None or type(prop) is not _data_type[type_name]:
                    m_props += "%s (%s), " % (name, type_name)
            if m_props:
                return _jsonify({"msg": "Missing '" + m_props[:m_props.rindex(",")] + "' key(s) in json data."}), 400
            return function()

        return wrapper

    return inner_function


def replace_last(string: str, old_str: str, new_str: str) -> str:
    ind = string.rfind(old_str)
    return string[:ind] + string[ind:].replace(old_str, new_str) if ind > -1 and ind != len(string) else string


def _parse_int(n):
    try:
        return int(float(n))
    except ValueError:
        return int(0)
