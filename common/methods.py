# PLACE ONLY STATIC/INDEPENDENT Classes/Functions... here !

from flask import request, jsonify
from functools import wraps


def props_required(*args):
    def inner_function(function):
        @wraps(function)
        def wrapper():
            content_type = request.headers.get("Content-Type")
            if not content_type or type(content_type) is not str or content_type.lower().strip() != "application/json":
                return jsonify({"msg": "Missing Header: 'Content-Type': 'application/json'"}), 400
            del content_type
            types = {
                "str": str,
                "int": int,
                "bool": bool,
                "dict": dict,
                "list": list,
                "float": float
            }
            m_props = ""  # missing props
            for arg in args:
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
                prop = request.json.get(name)
                if prop is None or type(prop) is not types[type_name]:
                    m_props += "%s (%s), " % (name, type_name)
            if m_props:
                return jsonify({"msg": "Missing '" + m_props[:m_props.rindex(",")] + "' key(s) in json data."}), 400
            return function()

        return wrapper

    return inner_function


def replace_last(string: str, old_str: str, new_str: str) -> str:
    ind = string.rfind(old_str)
    return string[:ind] + string[ind:].replace(old_str, new_str) if ind > -1 and ind != len(string) else string
