mod_def = {}

mod_def["FILES"] = {
    "PARENT": None,
    "PRIORITY": 10,
    "MENU": 2,
    "ICON": "file",
    "NAME": "FILES",
    "TABLE": "FILES",
    "ROW_NAME": "FILES_ID",
    "DEFAULT_COLS": ["FILES_TABLE",
                     "FILES_ROWID",
                     "FILES_COLUMN",
                     "FILES_DATA"],
    "NEW": 0,
    "UDF": 0,
    "ORDER": ["FILES_TABLE", "FILES_ROW_ID", "FILES_COLUMN"],
    "INDEX": [],
    "UNIQUE": [["FILES_TABLE", "FILES_ROWID", "FILES_COLUMN"]],
    "AUTH": {
        "READ": 100,
        "WRITE": 100,
        "INSERT": 100,
        "DELETE": 100,
    }
    "COLS": [
        {
            "CATEGORY": "FILE",
            "NAME": "FILES_TABLE",
            "HEADER": "TABLE",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 0,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 1,
            "DEFAULT": None,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
        {
            "CATEGORY": "FILE",
            "NAME": "FILES_ROWID",
            "HEADER": "ROWID",
            "TYPE": "INT",
            "EDIT": 0,
            "QUERY": 1,
            "SEARCH": 0,
            "REQUIRED": 1,
            "DEFAULT": None,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
        {
            "CATEGORY": "FILE",
            "NAME": "FILES_COLUMN",
            "HEADER": "COLUMN",
            "TYPE": "CHAR",
            "SIZE": 25,
            "EDIT": 0,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 1,
            "DEFAULT": None,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
        {
            "CATEGORY": "FILE",
            "NAME": "FILES_DATA",
            "HEADER": "DATA",
            "TYPE": "FILE",
            "EDIT": 0,
            "QUERY": 0,
            "SEARCH": 0,
            "REQUIRED": 1,
            "DEFAULT": None,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
        {
            "CATEGORY": "FILE",
            "NAME": "FILES_EXT",
            "HEADER": "EXT",
            "TYPE": "CHAR",
            "SIZE": 5,
            "EDIT": 0,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 0,
            "DEFAULT": None,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
        {
            "CATEGORY": "FILE",
            "NAME": "FILES_MIMETYPE",
            "HEADER": "MIMETYPE",
            "TYPE": "CHAR",
            "SIZE": 50,
            "EDIT": 0,
            "QUERY": 1,
            "SEARCH": 1,
            "REQUIRED": 1,
            "DEFAULT": None,
            "NEW": 0,
            "AUTH": {
                "READ": 100,
                "WRITE": 100,
            }
        },
    ]
}
