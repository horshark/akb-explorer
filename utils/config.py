import json

config_file = "config.json"
token = [t.replace("\n","") for t in open("api.txt","r")][0]

base_url = ""
headers = ""

with open(config_file) as json_file:
    data = json.load(json_file)

    base_url = data["base_url"]
    headers = data["headers"]
    headers["Authorization"] += token