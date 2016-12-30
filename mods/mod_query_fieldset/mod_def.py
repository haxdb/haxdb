mod_def = {}

mod_def["QUERY"] = {
    "NAME": "QUERY",
    "TABLE": "QUERY",
    "ROWID": "QUERY_ID",
    "CONTEXT_ROW": None,
    "COLS": [
        {
         "NAME": "QUERY_NAME",
         "HEADER": "NAME",
         "TYPE": "STR",
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 1,
         "INTERNAL": 0,
        },
        {
         "NAME": "QUERY_PEOPLE_ID",
         "HEADER": "OWNER",
         "TYPE": "ID",
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "NAME": "QUERY_CONTEXT",
         "HEADER": "CONTEXT",
         "TYPE": "CHAR",
         "SIZE": 50,
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "NAME": "QUERY_CONTEXT_ID",
         "HEADER": "CONTEXT_ID",
         "TYPE": "ID",
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "NAME": "QUERY_QUERY",
         "HEADER": "QUERY",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "INTERNAL": 0,
        },
        {
         "NAME": "QUERY_ORDER",
         "HEADER": "ORDER",
         "TYPE": "FLOAT",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
        },
    ],
    "ORDER": ["QUERY_ORDER", "QUERY_NAME"]
}

mod_def["FIELDSET"] = {
    "NAME": "FIELDSET",
    "TABLE": "FIELDSET",
    "ROWID": "FIELDSET_ID",
    "CONTEXT_ROW": None,
    "COLS": [
        {
         "NAME": "FIELDSET_NAME",
         "HEADER": "NAME",
         "TYPE": "STR",
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 1,
         "INTERNAL": 0,
        },
        {
         "NAME": "FIELDSET_PEOPLE_ID",
         "HEADER": "OWNER",
         "TYPE": "ID",
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "NAME": "FIELDSET_CONTEXT",
         "HEADER": "CONTEXT",
         "TYPE": "CHAR",
         "SIZE": 50,
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "NAME": "FIELDSET_CONTEXT_ID",
         "HEADER": "CONTEXT_ID",
         "TYPE": "ID",
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "NAME": "FIELDSET_ORDER",
         "HEADER": "ORDER",
         "TYPE": "FLOAT",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
        },
    ],
    "ORDER": ["FIELDSET_ORDER", "FIELDSET_NAME"]
}