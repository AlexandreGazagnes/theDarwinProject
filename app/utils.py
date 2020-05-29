import datetime
import secrets
from flask import session


def now():
    return str(datetime.datetime.now())[:19]


def manage_session(route):
    """manage session data"""

    if not session.get("sess_id"):
        session["sess_id"] = secrets.token_hex(16)
        session["page_count"] = 1
        session["hits"] = [
            (now(), route),
        ]
    else:
        session["page_count"] += 1
        session["hits"].append((now(), route))
