mod_def = {}

mod_def["NODES"] = {
    "NAME": "NODES",
    "TABLE": "NODES",
    "ROWID": "NODES_ID",
    "CONTEXT_ROW": None,
    "COLS": [
        {
         "NAME": "NODES_API_KEY",
         "HEADER": "API_KEY",
         "TYPE": "ASCII",
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
        },
        {
         "NAME": "NODES_NAME",
         "HEADER": "NAME",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "DEFAULT": 1,
         "NEW": 1,
        },
        {
         "NAME": "NODES_DESCRIPTION",
         "HEADER": "DESCRIPTION",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "NAME": "NODES_READONLY",
         "HEADER": "READONLY",
         "TYPE": "BOOL",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "DEFAULT": 1,
         "NEW": 1,
        },
        {
         "NAME": "NODES_DBA",
         "HEADER": "DBA",
         "TYPE": "BOOL",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "DEFAULT": 1,
         "NEW": 1,
        },
        {
         "NAME": "NODES_IP",
         "HEADER": "IP",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "DEFAULT": 1,
         "NEW": 1,
        },
        {
         "NAME": "NODES_EXPIRE",
         "HEADER": "EXPIRE",
         "TYPE": "TIMESTAMP",
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "DEFAULT": 1,
        },
        {
         "NAME": "NODES_ENABLED",
         "HEADER": "ENABLED",
         "TYPE": "BOOL",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "DEFAULT": 1,
         "NEW": 1,
         "DEFAULT_VALUE": 1,
        },
        {
         "NAME": "NODES_QUEUED",
         "HEADER": "QUEUED",
         "TYPE": "BOOL",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
        },
        {
         "NAME": "NODES_PEOPLE_ID",
         "HEADER": "PERSON",
         "TYPE": "ID",
         "ID_API": "PEOPLE",
         "ID_ID": "PEOPLE_ID",
         "ID_VIEW": ["PEOPLE_NAME_FIRST", "PEOPLE_NAME_LAST"],
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 0,
        },
        {
         "NAME": "NODES_ASSETS_ID",
         "HEADER": "ASSET",
         "TYPE": "ID",
         "ID_API": "ASSETS",
         "ID_ID": "ASSETS_ID",
         "ID_VIEW": ["ASSETS_NAME"],
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 0,
        },
    ],
    "ORDER": ["NODES_NAME"]
}
