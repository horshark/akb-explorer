# AKB-Explorer
A command line tool to search AttackerKB.

# How to install
Not much to do, you just have to clone the repo and install the required python libraries.
```bash
git clone https://github.com/horshark/akb-explorer/
pip install -r requirements.txt
```
Then you need to add your AKB API key in ``config/api.txt``. You can retrive it from your AKB profile.
```bash
echo "YOUR_AKB_API_KEY_HERE" > config/api.txt
```
And you are done! :)

# How to use
This is the help command:
```
python3 .\akb-explorer.py -h
usage: akb-explorer.py [-h] [-q QUERY] [-cve CVE] [-u USER]

Search through AttackerKB via command line!

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Search for a topic (by keywords or CVE-YEAR-XXXX)
  -cve CVE, --cve CVE   Search for a CVE using it's code (CVE-YEAR-XXXX)
  -u USER, --username USER
                        Search for a user
```

And below are a few explicit examples.
* To query using keywords:
```bash
python3 .\akb-explorer.py -q blue
```
* To search for a specific CVE: 
***(it actually does the same at -q but formatted differently, giving something else than a CVE will cause errors for now.)***
```bash
python3 .\akb-explorer.py -cve CVE-2020-0688
```
* To look for a user.
```bash
python3 .\akb-explorer.py -u horshark
```

# Credits
Thanks to @kevthehermit for helping me simplify my tool using his [python library](https://github.com/kevthehermit/attackerkb-api)!

# Related projects
* [AttackerKB Discord BOT](https://github.com/horshark/akb-discord-bot)
