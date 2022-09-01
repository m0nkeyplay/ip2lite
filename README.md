# ip2lite
use the IP2 Location Lite DB to search for IPs in an area

Created for the IP2LOCATION PROGRAMMING CONTEST 2022
https://contest.ip2location.com/

Sign up to download a copy of the database here.  https://lite.ip2location.com/.  A copy of the database is not included in this repo.

Included are a python script to be run locally with a copy of the IP2 Location Lite DB.

getLocationIP.py

Provide the path to the DB, what City/Region/Country you would like to search and choose an exact match or a general match and get back a C Class of IPs per region.  

[![asciicast](https://asciinema.org/a/n0LdGAFTXTG04aepmennnvGU7.svg)](https://asciinema.org/a/n0LdGAFTXTG04aepmennnvGU7)


Since people also like web pages, there is a web version built with python and Flask that will provide the same information.  This can be viewed at https://ip2.themonkeyplayground.com. If using this, one will probably want to take out the links to my web site hard coded in it.

Update guniConf.ini with ports you wish to use then run startweb.sh and it's up.


