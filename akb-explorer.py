import argparse, cgi, json

from attackerkb_api import AttackerKB

import utils.config as config
from utils.sanitizer import sanitize
from utils.printer import *


def hasResult(data):
    if data == None or len(data) == 0:
        print("Sorry, nothing found. Please check the filters or try with another query.")
        return False
    return True


def main():
    # Printing the banner.
    print(config.get_banner())

    api_key = config.token
    if api_key:
        api = AttackerKB(api_key)

    # Retrieving needed config.
    sortTypesConfig = config.get("sort")
    sortTypes = sortTypesConfig["tags"] + sortTypesConfig["score"]
    sortTypesDesc = sortTypesConfig["description"]

    # Parsing args.
    parser = argparse.ArgumentParser(description='Search through AttackerKB via command line!')
    
    ## Making groups.
    group_search = parser.add_argument_group("Search arguments", "Query using keywords, CVEs or usernames.")
    group_filter = parser.add_argument_group("Filter arguments", "Sort and filter your query's results using tags and scores.")

    mg_search = group_search.add_mutually_exclusive_group()
    mg_filter = group_filter.add_mutually_exclusive_group()

    ## Searching arguments.
    mg_search.add_argument("-q", "--query", dest="query", metavar="KEYWORDS", help="Search for a topic using keywords")
    mg_search.add_argument("-cve", "--cve", dest="cve", metavar="CVE-YEAR-XXXX", help="Search for a CVE using its code")
    mg_search.add_argument("-u", "--username", dest="user", metavar="USERNAME", help="Search for a user")
    
    ## Filtering args.
    mg_filter.add_argument("-s", "--sort", choices=sortTypes, metavar="VALUE", dest="sort", help="Let you sort topics using a specified field ascendingly")
    mg_filter.add_argument("-r", "--rev-sort", choices=sortTypes, metavar="VALUE", dest="rsort", help="Let you sort topics using a specified field descendingly")

    parser.add_argument("-l", "--list", action='store_true',  help="Display every sorting and filter values.")


    args = parser.parse_args()

    current_data = None

    # Handles the sorting options.
    doSort = False
    sortAsc = True
    sortTag = None

    if args.sort:
        doSort = True
        sortTag = args.sort
    if args.rsort:
        doSort = True
        sortAsc = False
        sortTag = args.rsort

    # Calls fitting module.
    ## Listing
    if args.list == True:
        print("Tags allow you to both filter and sort. \nHere is the list of every tags:\n" + print_tags(sortTypesConfig["tags"], sortTypesDesc))
        print("\nHere are values that only supports sorting:\n" + print_tags(sortTypesConfig["score"], sortTypesDesc))
        exit(0)

    ## Queries
    elif args.query:
        max_len = 5

        if doSort:
            sort_filter = '{0}:{1}'.format(sortTag, 'asc' if sortAsc else 'desc')
            current_data = api.get_topics(sort=sort_filter, q=args.query)
            
        else:
            current_data = api.get_topics(q=args.query, size=max_len)

        if hasResult(current_data):

            if len(current_data) < max_len:
                max_len = len(current_data)
                
            for i in range(max_len, 0, -1):
                print_topic_short(current_data, i=i-1)
                print("--- ("+ str(i) +") for more details -- (else) to leave")
            
            # int() doesn't like empty strings, so if sanitize returns an empty string;
            # answer will be -1 which will cause the program to exit.
            try:
                answer = int(sanitize(input()))
            except:
                answer = -1

            if answer >= 1 and answer <= max_len:
                clear()
                print_topic_long(current_data, i=answer-1)

    ## CVE
    elif args.cve:
        if doSort:
            sort_filter = '{0}:{1}'.format(sortTag, 'asc' if sortAsc else 'desc')
            current_data = api.get_topics(sort=sort_filter, name=args.cve)
        else:
            current_data = api.get_topics(name=args.cve)

        if hasResult(current_data):
            print_topic_short(current_data, cve=args.cve)
            print("--- (+) for more details -- (else) to leave")

            answer = input()

            if sanitize(answer) == "+":
                clear()
                print_topic_long(current_data, cve=args.cve)

    ## Users
    elif args.user:
        current_data = api.get_single_contributor(args.user)

        if hasResult(current_data):
            print_contributor(current_data)

    ## Nothing, print help message.
    else:
        print("No argument found. Try using -h to get help.")

if __name__ == "__main__":
    main()
