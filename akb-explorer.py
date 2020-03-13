import argparse, cgi, json


from modules.contributors import *
from modules.topics import *

from utils.sanitizer import sanitize
from utils.printer import *


def hasResult(data):
    if data == None or len(data) == 0:
        print("Sorry, nothing found. Please try with another query.")
        return False
    return True


def main():

    # Parsing args.
    parser = argparse.ArgumentParser(description='Search through AttackerKB via command line!')

    parser.add_argument("-q", "--query", dest="query", help="Search for a topic (by keywords or CVE-YEAR-XXXX)")
    parser.add_argument("-cve", "--cve", dest="cve", help="Search for a CVE using it's code (CVE-YEAR-XXXX)")
    parser.add_argument("-u", "--username", dest="user", help="Search for a user")

    args = parser.parse_args()

    current_data = None

    # Calls fitting module.
    ## Queries
    if args.query:
        current_data = get_from_name(args.query)

        if hasResult(current_data):
            l = 5

            if len(current_data) < 5:
                l = len(current_data)
                
            for i in range(l,0,-1):
                print_topic_short(current_data, i=i-1)
                print("--- ("+ str(i) +") for more details -- (else) to leave")
            
            answer = int(sanitize(input()))

            if answer >= 1 and answer <= l:
                clear()
                print_topic_long(current_data, i=answer-1)

    ## CVE
    elif args.cve:
        current_data = get_from_name(args.cve)

        if hasResult(current_data):
            print_topic_short(current_data, cve=args.cve)
            print("--- (+) for more details -- (else) to leave")

            answer = input()

            if sanitize(answer) == "+":
                clear()
                print_topic_long(current_data, cve=args.cve)

    ## Users
    elif args.user:
        current_data = get_from_username(args.user)

        if hasResult(current_data):
            print_contributor(current_data)


if __name__ == "__main__":
    main()
