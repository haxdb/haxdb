import mod_db
import mod_api
import mod_def


def init(haxdb):
    mod_db.init(haxdb)
    mod_api.init(haxdb, config)
    return mod_def.mod_def


def run():
    mod_db.run()
    mod_api.run()
