import requests

from utils.sanitizer import sanitize

import utils.config as config

# Config.
sortTypesConfig = config.get("sort")
sortTypes = sortTypesConfig["tags"] + sortTypesConfig["score"]

def add_sorting(query, sort, asc):

    # Direction to sort in.
    direction = "asc"

    if asc == False:
        direction = "desc"

    query += "&sort="+sort+":"+direction

    return query


def get_from_name(name, sort=None, sortAsc=None):
    name = sanitize(name)

    # Creating the request.
    request = config.base_url + "topics?q=" + name

    # If sorting is enabled.
    if sort != None and sortAsc != None:
        request = add_sorting(request, sort, sortAsc)

    # Ending the request.
    request += "&qt=search"

    r = requests.get(request, headers=config.headers)

    json = r.json()

    # In case we get an error, the API returns a status and a message.
    if "status" in json:
        print("[ERRROR] AKB: " + json["message"])
        return None

    topics = json["data"]

    return topics