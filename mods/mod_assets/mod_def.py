mod_def = {}

mod_def["ASSETS"] = {
    "NAME": "ASSETS",
    "TABLE": "ASSETS",
    "ROWID": "ASSETS_ID",
    "CONTEXT_ROW": None,
    "COLS": [
        {
         "NAME": "ASSETS_NAME",
         "HEADER": "NAME",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 1,
        },
        {
         "NAME": "ASSETS_TYPE",
         "HEADER": "TYPE",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "NAME": "ASSETS_MANUFACTURER",
         "HEADER": "MANUFACTURER",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "NAME": "ASSETS_MODEL",
         "HEADER": "MODEL",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "NAME": "ASSETS_QUANTITY",
         "HEADER": "QTY",
         "TYPE": "INT",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "NAME": "ASSETS_LOCATION",
         "HEADER": "LOCATION",
         "TYPE": "LIST",
         "EDIT": 1,
         "LIST_NAME": "ASSET LOCATIONS",
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "NAME": "ASSETS_DESCRIPTION",
         "HEADER": "DESCRIPTION",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
    ],
    "ORDER": ["ASSETS_NAME"]
}

mod_def["ASSET_LINKS"] = {
    "NAME": "ASSET_LINKS",
    "TABLE": "ASSET_LINKS",
    "ROWID": "ASSET_LINKS_ID",
    "CONTEXT_ROW": None,
    "COLS": [
        {
         "NAME": "ASSET_LINKS_NAME",
         "HEADER": "NAME",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 1,
        },
        {
         "NAME": "ASSET_LINKS_LINK",
         "HEADER": "URL",
         "TYPE": "STR",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "NAME": "ASSET_LINKS_ORDER",
         "HEADER": "ORDER",
         "TYPE": "FLOAT",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
    ],
    "ORDER": ["ASSET_LINKS_NAME"]
}

mod_def["ASSET_AUTHS"] = {
    "NAME": "ASSET_AUTHS",
    "TABLE": "ASSET_AUTHS",
    "ROWID": "ASSET_AUTHS_ID",
    "CONTEXT_ROW": None,
    "COLS": [
        {
         "NAME": "PEOPLE_NAME_LAST",
         "HEADER": "LAST",
         "TYPE": "STR",
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "NAME": "PEOPLE_NAME_FIRST",
         "HEADER": "FIRST",
         "TYPE": "STR",
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "NAME": "ASSET_AUTHS_ENABLED",
         "HEADER": "ENABLED",
         "TYPE": "BOOL",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
    ],
    "ORDER": ["ASSET_LINKS_NAME"]
}