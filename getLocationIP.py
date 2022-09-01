#!/usr/bin/env python3

from os import path as op
import signal
import csv

#   CTRL+C handler - from https:/gist.github.com/mikerr/6389549
def handler(signum, frame):
    print("\n^^^^^^Task aborted by user.  Some cleanup may be necessary.")
    exit(0)

signal.signal(signal.SIGINT,handler)

chatter = """
########################################
#   Get Location IPs
#
#   Grab a C Class from the country, region, city searched for 
#   Provides ips, country, region, city
#   This uses IP2LOCATION-LITE-DB3.CSV from
#   https://lite.ip2location.com/ to do this
#
#   https://www.themonkeyplayground.com
#   https://github.com/m0nkeyplay/getthatlocationips
#######################################
"""

working = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Searching for: %s

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Results:
"""
def long2DotIP(ipnum):
    return str(int(ipnum / 16777216) % 256) + "." \
        + str(int(ipnum / 65536) % 256) + "." \
        + str(int(ipnum / 256) % 256) + "." \
        + str(int(ipnum % 256))

def showIt(region,myArray,myResult):
    if region in myArray:
        True
    else:
        myArray.append(region)
        beg = long2DotIP(int(myResult[0]))
        end = long2DotIP(int(myResult[1]))
        cc = myResult[2]
        country = myResult[3]
        city = myResult[5]
        returnMe = "%s, %s - %s(%s) : %s-%s"%(city,region,country,cc,beg,end)
        print(returnMe)

def lookUpPlace(daFile,daSearch,eqo):
    x = 0
    daRegionArray = []
    csv_file = csv.reader(open(daFile, "r"), delimiter=",")
    print(working%daSearch)
    for row in csv_file:
        daRegion = row[4]
        if eqo == "e":
            if daSearch == row[5].lower() or daSearch == row[4].lower() or daSearch == row[3].lower():
                x+=1
                showIt(daRegion,daRegionArray,row)
        else:
            if daSearch in row[5].lower() or daSearch in row[4].lower() or daSearch in row[3].lower():
                x+=1
                showIt(daRegion,daRegionArray,row)
    if x == 0:
        print("No results found for %s.  Check spelling and/or try not to abbreviate?"%daSearch)


if __name__ == '__main__':
    print(chatter)
    fileN = input("Name and location of IP2LOCATION-LITE csv file: ")
    if not op.isfile(fileN):
        print("We can't find the IP2LOCATION-LITE csv file. Please check the path/file")
        exit()
    searchMe = input("City/Region/Country: ") 
    search = searchMe.strip().lower()
    eo = input("Equals (e) OR Like (l): ")
    if eo == "e" or eo == "l":
        lookUpPlace(fileN,search,eo)
    else:
        print("-el needs to be e or l.  Thanks. Try again.")