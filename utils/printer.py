import platform, os


#########################################################################################
#                                                                                       #
#             This whole file needs to be cleaned, re-written and optimized.            #
#   The reason it's so ugly is because I wrote it while trying to make it look good;    #
#  be efficient and clean for the user, that implies a lot has changed in the program;  #
#                           since the first line were written etc.                      #
#      So yes, I know it's ugly and I need to sit down and re-write it from scratch.    #
#                                                                                       #
#########################################################################################


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def print_json(json):
    
    margin = 2
    key_offset = 3 + margin

    for key in json[0]:
        key_l = len(key) + margin

        if key_l > key_offset:
            key_offset = key_l
    
    print("\nTITLE" + (key_offset-5)*" " + "| VALUE")
    print("-" * (key_offset + 60))

    for key in json[0]:
        print(key.upper() + (key_offset-len(key))*" " + "| " + str(json[0][key]))
    
    print("") # New line.

def print_tags(items, desc):
    s = ""

    max_len = len(max(items, key=len))

    for i in items:
        # offset = (1 + max_len - len(i))*" "
        # line = "\t" + i + offset + "| " + desc[i] + "\n"

        offset = (max_len - len(i))*" "
        line = "\t" + offset + i + " | " + desc[i] + "\n"

        s += line

    return s
    # separator = '\t\t | \t\t'

    # s = ""
    # size = len(items)

    # for i in range(0, size):
    #     item = items[i]
    #     s += item
    #     if(not i == size-1):
    #         s += item + separator+ desc[item] + "\n"

    # return s

def print_contributor(json):
    
    prefix = 2
    margin = 5

    key_offset = 3 + margin

    items = {
            "Username":json["username"],
            "Score":json["score"],
            "Link":"https://attackerkb.com/contributors/"+json["username"],
            "Id":json["id"]
            }

    for key in items:
        key_l = len(key) + margin

        if key_l > key_offset:
            key_offset = key_l
    
    print("\nTITLE" + (key_offset-5)*" " + "| VALUE")
    print("-" * (key_offset + 80))

    for key in items:
        str_prefix = " " * prefix
        str_suffix = " " * (key_offset-(len(key)+prefix))
        mid = "| "

        key_up = key.upper()
        data = str(items[key])

        print(str_prefix + key_up + str_suffix + mid + str_prefix + data)
    
    print("") # New line.

def print_topic_short(json, i=0, cve=None):

    prefix = 2
    margin = 5

    key_offset = 3 + margin

    items = {
            "Name":json[i]["name"][0:50],
            "CVE":cve,
            "Date":json[i]["created"][0:10],
            "Link":"https://attackerkb.com/topics/"+json[i]["id"],
            "Id":json[i]["id"],
            "Score":"AV: "+str(round(json[i]["score"]["attackerValue"], 1)) + " | Exp: "+str(round(json[i]["score"]["exploitability"], 1)),
            "Description":json[i]["document"][0:75]
            }

    if cve:
        items.update({"Mitre Link":"https://cve.mitre.org/cgi-bin/cvename.cgi?name="+cve})
        items.pop("Name", None)

    for key in items:
        key_l = len(key) + margin

        if key_l > key_offset:
            key_offset = key_l
    
    print("\nTITLE" + (key_offset-5)*" " + "| VALUE")
    print("-" * (key_offset + 80))

    for key in items:
        str_prefix = " " * prefix
        str_suffix = " " * (key_offset-(len(key)+prefix))
        mid = "| "

        key_up = key.upper()
        data = str(items[key])

        if (key == "CVE" and cve != None) or key != "CVE":
            print(str_prefix + key_up + str_suffix + mid + str_prefix + data)
    
    print("") # New line.

def print_topic_long(json, i=0, cve=None):
    
    line = "-"
    mid = "| "

    prefix = 2
    margin = 5

    key_offset = 3 + margin

    data = json[i]
    data_tag = data['tags']
    
    # Need to clean this mess.
    items = {
            "Name":data["name"][0:50],
            "CVE":cve,
            "Date":data["created"][0:10],
            "Link":"https://attackerkb.com/topics/"+data["id"],
            "Id":data["id"],
            # "Editor":,
            "Editor Id":data["editorId"],
            "Score":"AV: "+str(round(data["score"]["attackerValue"], 1)) + " | Exp: "+str(round(data["score"]["exploitability"], 1)),
            "Description":data["document"][0:75],
            " ":data["document"][75:150],
            "Mitre Link":"",
            "High value":"Enterprise: "+str(round(data_tag['commonEnterprise'], 1)) + 
            " | Default config: "+str(round(data_tag['defaultConfiguration'], 1)) +
            " | Patch difficulty: "+str(round(data_tag['difficultToPatch'], 1)),
            "  ":"High priv: "+str(round(data_tag['highPrivilegeAccess'], 1)) + 
            " | Easy dev: "+str(round(data_tag['easyToDevelop'], 1)) +
            " | No auth: "+str(round(data_tag['preAuth'], 1)),
            "Low value":"Requires interation: "+str(round(data_tag['requiresInteraction'], 1)) +
            " | Obscure config: "+str(round(data_tag['obscureConfiguration'], 1)) + 
            " | Exp. difficulty: "+str(round(data_tag['difficultToExploit'], 1)) +
            " | No useful data: "+str(round(data_tag['noUsefulData'], 1)),
            "   ":"Difficult dev: "+str(round(data_tag['difficultToDevelop'], 1)) + 
            " | Needs auth: "+str(round(data_tag['postAuth'], 1))
            }

    if cve:
        items.update({"Mitre Link":"https://cve.mitre.org/cgi-bin/cvename.cgi?name="+cve})
        items.pop("Name", None)
    else:
        items.pop("Mitre Link", None)

    for key in items:
        key_l = len(key) + margin

        if key_l > key_offset:
            key_offset = key_l
    
    seperator = line * (key_offset + 80)

    print("\nTITLE" + (key_offset-5)*" " + "| VALUE")
    print(seperator)

    for key in items:
        str_prefix = " " * prefix
        str_suffix = " " * (key_offset-(len(key)+prefix))

        key_up = key.upper()
        data = str(items[key])

        if key == "High value" or key == "Low value":
            print(seperator)

        if (key == "CVE" and cve != None) or key != "CVE":
            print(str_prefix + key_up + str_suffix + mid + str_prefix + data)
    
    print("") # New line.