import requests

from utils.sanitizer import sanitize

import utils.config as config

def get_from_name(name):
    name = sanitize(name)

    r = requests.get(config.base_url+"topics?q="+name+"&qt=search", headers=config.headers)
    
    json = r.json()

    topic = json["data"]

    return topic