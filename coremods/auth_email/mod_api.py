import os
import base64
import json
import time
import re
from flask import request

haxdb = None
db = None
config = None
tools = None


def init(app_haxdb, mod_config, mod_tools):
    global haxdb, db, config, tools
    haxdb = app_haxdb
    tools = mod_tools
    db = haxdb.db
    config = mod_config


def run():
    global haxdb, config, db, tools

    @haxdb.app.route("/AUTH/email/login", methods=["GET", "POST"])
    @haxdb.app.route("/AUTH/email/login/<email>", methods=["GET", "POST"])
    def mod_auth_email(email=None):
        email = email or haxdb.get("email")
        subject = haxdb.get("subject")
        message = haxdb.get("message")
        email = email.upper()

        meta = {}
        meta["api"] = "AUTH/email"
        meta["action"] = "login"
        meta["email"] = email

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return haxdb.output(success=0,
                                message="INVALID VALUE: email",
                                meta=meta)

        # EMAIL EXISTS%s
        sql = "SELECT * FROM PEOPLE WHERE PEOPLE_EMAIL = %s"
        people = db.qaf(sql, (email,))
        if not people:
            return haxdb.output(success=0,
                                value=1,
                                message="NEW USER",
                                meta=meta)

        # CREATE TOKEN
        token = base64.urlsafe_b64encode(os.urandom(500))[5:39]
        expire = time.time() + int(config["AUTH"]["TOKEN_EXPIRE"])
        sql = """
        INSERT INTO AUTH_TOKEN
        (AUTH_TOKEN_TOKEN, AUTH_TOKEN_PEOPLE_ID, AUTH_TOKEN_EXPIRE)
        VALUES (%s,%s,%s)
        """
        db.query(sql, (token, people["PEOPLE_ID"], expire))
        if db.error:
            return haxdb.output(success=0, message=db.error, meta=meta)
        db.commit()

        to = "{} {} <{}>".format(people["PEOPLE_NAME_FIRST"],
                                 people["PEOPLE_NAME_LAST"],
                                 people["PEOPLE_EMAIL"])
        message = message.replace("[token]", token)
        result = tools.send_email(to, subject, message)
        if not result:
            return haxdb.output(success=0, message=result, meta=meta)
        return haxdb.output(success=1, message="EMAIL SENT", meta=meta)

    @haxdb.app.route("/AUTH/email/register", methods=["GET", "POST"])
    @haxdb.app.route("/AUTH/email/register/<email>", methods=["GET", "POST"])
    def mod_auth_register(email=None):
        email = email or haxdb.get("email")
        subject = haxdb.get("subject")
        message = haxdb.get("message")

        meta = {}
        meta["api"] = "AUTH/email"
        meta["action"] = "register"
        meta["email"] = email
        meta["subject"] = subject
        meta["message"] = message

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return haxdb.output(success=0,
                                message="INVALID VALUE: email",
                                meta=meta)

        email = email.upper()
        sql = "SELECT * FROM PEOPLE WHERE PEOPLE_EMAIL = %s"
        people = db.qaf(sql, (email,))
        if people:
            return haxdb.output(success=0,
                                message="USER ALREADY EXISTS",
                                meta=meta)

        sql = "INSERT INTO PEOPLE(PEOPLE_EMAIL) VALUES (%s)"
        db.query(sql, (email,))
        people_id = db.lastrowid
        db.commit()

        token = base64.urlsafe_b64encode(os.urandom(500))[5:39]
        expire = int(time.time()) + int(config["AUTH"]["TOKEN_EXPIRE"])
        sql = """
        INSERT INTO AUTH_TOKEN
        (AUTH_TOKEN_TOKEN, AUTH_TOKEN_PEOPLE_ID, AUTH_TOKEN_EXPIRE)
        VALUES (%s,%s,%s)
        """
        db.query(sql, (token, people_id, expire))
        if db.error:
            return haxdb.output(success=0, message=db.error, meta=meta)
        db.commit()

        to = email
        message = message.replace("[token]", token)
        result = tools.send_email(email, subject, message)

        if not result:
            return haxdb.output(success=0, message=result, meta=meta)
        return haxdb.output(success=1, message="EMAIL SENT", meta=meta)

    @haxdb.app.route("/AUTH/token", methods=["GET", "POST"])
    @haxdb.app.route("/AUTH/token/<token>", methods=["GET", "POST"])
    def mod_auth_token(token=None):
        token = token or haxdb.get("token")
        config_dbas = [x.strip().upper() for x in config["AUTH"]["DBA"].split(',')]
        now = int(time.time())

        meta = {}
        meta["api"] = "AUTH/email"
        meta["action"] = "token"
        meta["token"] = token

        # DELETE OLD TOKEN
        db.query("DELETE FROM AUTH_TOKEN WHERE AUTH_TOKEN_EXPIRE<%s", (now,))
        if db.error:
            return haxdb.output(success=0, message=db.error, meta=meta)
        db.commit()

        # VALIDATE TOKEN
        sql = """
        SELECT *
        FROM AUTH_TOKEN
        JOIN PEOPLE ON AUTH_TOKEN_PEOPLE_ID = PEOPLE_ID
        WHERE
        AUTH_TOKEN_TOKEN = %s
        AND AUTH_TOKEN_EXPIRE > %s
        """
        db.query(sql, (token, now,))
        row = db.next()
        if not row:
            msg = "TOKEN IS INVALID OR EXPIRED.\nLOG IN AGAIN."
            return haxdb.output(success=0, message=msg, meta=meta)

        # CREATE SESSION NODE
        api_key = base64.urlsafe_b64encode(os.urandom(500))[5:39]
        expire = int(time.time() + int(config["AUTH"]["TOKEN_EXPIRE"]))
        node_name = "{} {} TOKEN AUTH".format(row["PEOPLE_NAME_FIRST"],
                                              row["PEOPLE_NAME_LAST"],)
        dba = row["PEOPLE_DBA"]
        if row["PEOPLE_EMAIL"].upper() in config_dbas:
            dba = 1
        ip = str(request.access_route[-1])
        sql = """
        INSERT INTO NODES (NODES_API_KEY,NODES_PEOPLE_ID,NODES_NAME,
                           NODES_READONLY,NODES_DBA,NODES_IP,NODES_EXPIRE,
                           NODES_ENABLED,NODES_QUEUED)
        VALUES (%s,%s,%s,0,%s,%s,%s,1,0)
        """
        db.query(sql, (api_key, row["PEOPLE_ID"], node_name, dba, ip, expire,))
        if db.error:
            return haxdb.output(success=0, message=db.error, meta=meta)

        # REMOVE TOKEN
        sql = "DELETE FROM AUTH_TOKEN WHERE AUTH_TOKEN_TOKEN=%s"
        db.query(sql, (token,))
        if db.error:
            return haxdb.output(success=0, message=db.error, meta=meta)
        db.commit()

        meta["people_name"] = "{} {}".format(row["PEOPLE_NAME_FIRST"],
                                             row["PEOPLE_NAME_LAST"])
        return haxdb.output(success=1,
                            message="AUTHENTICATED",
                            meta=meta,
                            value=api_key)
