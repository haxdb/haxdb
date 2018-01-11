#! /usr/bin/env python

import logging
from config import config
import db
import haxdb
import haxdb_mods

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("gunicorn.error")

haxdb.init(config, db.db(config["DB"], logger), logger)
haxdb_mods.init(haxdb)
haxdb_mods.run()

app = haxdb.api_app
if __name__ == "__main__":
    haxdb.run()
