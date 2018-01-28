import base64

haxdb = None


def has_perm(table, perm_type, perm_val):
    if haxdb.session("dba") == 1:
        return True

    if perm_val <= 0:
        return True

    nodes_id = haxdb.session("nodes_id")
    sql = """
    SELECT * FROM NODESPERMS WHERE
    NODESPERMS_NODES_ID=%s
    AND NODESPERMS_TABLE=%s
    """
    row = haxdb.db.qaf(sql, (nodes_id, table))
    typecol = "NODESPERMS_{}".format(perm_type)

    try:
        if int(perm_val) <= int(row[typeocl]):
            return True
    except Exception:
        return False
    return False


def get_perm(table, perm_type):
    if haxdb.session("dba") == 1:
        return 99999999

    nodes_id = haxdb.session("nodes_id")
    sql = """
        SELECT * FROM NODESPERMS WHERE
        NODESPERMS_NODES_ID=%s
        AND NODESPERMS_TABLE=%s
    """
    row = haxdb.db.qaf(sql, (nodes_id, table))
    typecol = "NODESPERMS_{}".format(perm_type)
    try:
        return int(row[typecol])
    except Exception:
        return 0


def init(app_haxdb):
    global haxdb
    haxdb = app_haxdb


def run():
    haxdb.func("PERM:HAS", has_perm)
    haxdb.func("PERM:GET", get_perm)
