from functools import wraps
from flask import Flask, session
import os
from datetime import timedelta
from flask_cors import CORS
import data
import api

app = Flask("hdbapi")
app.secret_key = os.urandom(24)

VERSION = "v1"
config = None
db = None
logger = None
output = None
saved_functions = {}
saved_triggers = {}


def save_function(name, ref):
    saved_functions[name] = ref


def get_function(name):
    if name in saved_functions:
        return saved_functions[name]
    return None


def on(name, action, ref):
    if name not in saved_triggers:
        saved_triggers[name] = {}
    if action not in saved_triggers[name]:
        saved_triggers[name][action] = []
    saved_triggers[name][action].append(ref)


def trigger(name, action, context=None):
    logger.debug("TRIGGER: {}: {} ({})".format(name, action, context))
    try:
        funcs = saved_triggers[name][action]
    except KeyError:
        return False
    for func in funcs:
        try:
            func(context)
        except TypeError:
            msg = "INVALID TRIGGER FUNCTION FOR: {} {} ".format(name, action)
            logger.error(msg)


def init(app_config, app_db, app_logger):
    global config, db, api, logger
    config = app_config
    db = app_db
    logger = app_logger
    api.init(db)
    output = api.output


def run():
    debug = (int(config["API"]["DEBUG"]) == 1)
    CORS(app, origin=config["API"]["ORIGINS"])
    timeout = config["API"]["SESSION_TIMEOUT"]
    app.permanent_session_lifetime = timedelta(seconds=int(timeout))
    app.run(config["API"]["HOST"], int(config["API"]["PORT"]), debug=debug)


@app.before_request
def open_db():
    db.open()


@app.teardown_appcontext
def close_db(error):
    db.close()


def require_auth(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        session.permanent = True
        key = data.session.get("api_key")
        authenticated = data.session.get("api_authenticated")

        if not (key and authenticated == 1):
            msg = "NOT AUTHENTICATED"
            return output(success=0, message=msg, authenticated=False)
        return view_function(*args, **kwargs)

    return decorated_function


def require_dba(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        session.permanent = True
        dba = data.session.get("api_dba")
        if (not dba or (dba and int(dba) != 1)):
            return output(success=0, message="INVALID PERMISSION")
        return view_function(*args, **kwargs)

    return decorated_function


def no_readonly(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        session.permanent = True
        readonly = data.session.get("api_readonly")

        if (readonly and readonly == 1):
            return output(success=0, message="INVALID PERMISSION")
        return view_function(*args, **kwargs)

    return decorated_function
