import json

# Config initialization.
def file_not_found(file, message="Uh-oh, looks like something broke. You probably should reclone the repo."):
    error_message = "File " + file + " not found, exiting."

    if message != None:
        error_message += "\n" + message

    print(error_message)
    quit()

token_file = "config/api.txt"
config_file = "config/config.json"

token = None
config = None

base_url = None
headers = None

## Loading API token from file.
try:
    token = [t.replace("\n","") for t in open(token_file,"r")][0]
except:
    file_not_found(token_file, "Please put your API key in " + token_file)

## Loading config file.
try:
    with open(config_file) as json_file:
        config = json.load(json_file)

        base_url = config["base_url"]
        headers = config["headers"]
        headers["Authorization"] += token
except:
    file_not_found(config_file)


# Functions to retrieve data.
def get_banner():
    banner_file = config["banner"]

    try:
        banner = open(banner_file).read()
    except:
        file_not_found(banner_file)

    return banner

def get(key):
    try:
        ret = config[key]
    except:
        print("ERROR: couldn't not find key " + key + " in config.")
    
    return ret