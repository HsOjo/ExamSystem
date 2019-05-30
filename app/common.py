from flask import url_for


def check_rule_valid(rule: str):
    try:
        url_for(rule)
        return True
    except:
        return False
