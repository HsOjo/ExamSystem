import json

from flask import url_for


def check_rule_valid(rule: str):
    try:
        url_for(rule)
        return True
    except:
        return False


def json_load(*args, **kwargs):
    return json.loads(*args, **kwargs)


def json_dump(*args, **kwargs):
    return json.dumps(*args, **kwargs)


def alpha_num(num):
    return chr(ord('A') + num)
