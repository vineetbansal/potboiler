__version__ = "0.1.0"


import os
import logging.config
import logging
from types import SimpleNamespace
import json
from importlib_resources import read_text

import potboiler 


def hello():
    return "Hello World"


def setup_config():
    s = read_text(potboiler, 'config.json')
    d = json.loads(s)

    # logging.config doesn't support configuration from an object, but does support dictConfig,
    # so use the dict obtained from json.
    if 'logging' in d:
        logging.config.dictConfig(d['logging'])
    else:
        logging.basicConfig(level=logging.INFO)

    # Now that logging is configured, reload the json, but now with an object hook
    # so we have cleaner access to keys by way of attributes.
    # For string-type values, we try to expand them using environment variables
    # This allows us to have format-specifier style values in the json, like:
    # ..
    # "DB_URI": "mysql://{DBUSER}:{DBPASS}",
    # ..
    # For non-string type values, (this include SimpleNamespace type itself), we simply get the value as is,
    # allowing us chained attribute access).
    try:
        config = json.loads(
            s,
            object_hook=lambda d: SimpleNamespace(
                **{k: (v.format(**os.environ) if isinstance(v, str) else v) for k, v in d.items()}
            )
        )
    except KeyError as e:
        raise RuntimeError(f'Environment variable {e.args[0]} missing')

    return config


config = setup_config()
