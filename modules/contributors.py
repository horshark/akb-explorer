import requests

import utils.config as config

from utils.sanitizer import sanitize

def get_from_username(user, sort):
    user = sanitize(user)

    r = requests.get(config.base_url+"contributors?username="+user, headers=config.headers)
    json = r.json()

    user = json["data"]

    return user