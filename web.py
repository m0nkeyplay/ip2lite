#!/usr/bin/env python3

import csv
from flask import Flask
from flask import request
from flask import Flask
app = Flask(__name__)

fileN = "IP2LOCATION-LITE-DB3.CSV/IP2LOCATION-LITE-DB3.CSV"

chatter = """
<p>########################################<br />
#   Get Location IPs</br />
#   <br />
#   Grab a C Class from the country, region, city searched for <br />
#   Provides ips, country, region, city<br />
#   This uses IP2LOCATION-LITE-DB3.CSV from<br />
#   <a href="https://lite.ip2location.com/">https://lite.ip2location.com/</a> to do this<br />
#   <br />
#   <a href="https://www.themonkeyplayground.com">https://www.themonkeyplayground.com</a><br />
#   <a href="https://github.com/m0nkeyplay/ip2lite">https://github.com/m0nkeyplay/ip2lite</a><br />
<form action="s" method="POST">
City/Region/or Country to Search <input type="text" name="crc" /><br />
<select name="eorl">
<option value="e">Exact Match</option>
<option value="l">A Like Match</option>
</select><br />
<input type="submit" value="search"><br />
</form> 
#######################################
</p>
"""

work = """
<p>
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@<br />
Results:</p>
<table>
<tr>
<th>Location Info</th>
<th>A Subnet</th>
</tr>
"""

backHome = """
</table>
<hr />
<p><a href="https://ip2.themonkeyplayground.com">Back Home</a></p>
<p><a href="https://themonkeyplayground.com">The Monkey Playground</a></p>
"""

def long2DotIP(ipnum):
    return str(int(ipnum / 16777216) % 256) + "." \
        + str(int(ipnum / 65536) % 256) + "." \
        + str(int(ipnum / 256) % 256) + "." \
        + str(int(ipnum % 256))

def showIt(region,myArray,myResult):
    showMe = ""
    if region in myArray:
        True
    else:
        myArray.append(region)
        beg = long2DotIP(int(myResult[0]))
        end = long2DotIP(int(myResult[1]))
        cc = myResult[2]
        country = myResult[3]
        city = myResult[5]
        showMe += """
        <tr>
        <td>%s, %s - %s (%s)</td> 
        <td>%s-%s</td>
        </tr>"""%(city,region,country,cc,beg,end)
    return showMe

def lookUpPlace(daFile,daSearch,eqo):
    x = 0
    daRegion = ""
    daRegionArray = []
    csv_file = csv.reader(open(daFile, "r"), delimiter=",")
    showResults = work
    for row in csv_file:
        daRegion = row[4]
        if eqo == "e":
            if daSearch == row[5].lower() or daSearch == row[4].lower() or daSearch == row[3].lower():
                x+=1
                showResults += showIt(daRegion,daRegionArray,row)
        else:
            if daSearch in row[5].lower() or daSearch in row[4].lower() or daSearch in row[3].lower():
                x+=1
                showResults += showIt(daRegion,daRegionArray,row)
    if x == 0:
        showResults += "No results found for "+daSearch+".  Check spelling and/or try not to abbreviate?"+backHome
    else:
        showResults += backHome
    print(showResults)
    return str(showResults)

@app.route('/',methods=['POST','GET'])
def hello_people():
    return chatter

@app.route('/s',methods=['POST'])
def search_it():
    if request.method == 'POST':
        if request.form['crc'] and (request.form['eorl'] == "e" or request.form['eorl'] == "l"):
            search = request.form['crc'].strip().lower()
            eo = request.form['eorl']
            return lookUpPlace(fileN,search,eo)
        else:
            return "The app didn't like the search criteria thrown at it.  Please try again."
        

@app.errorhandler(404)
def page_not_found(e):
    msg = "404 - What you are looking for is not here.<br /><br />"
    msg += "Let's try <a href='https://themonkeyplayground.com'>here</a>"
    return msg

@app.errorhandler(405)
def page_not_found(e):
    msg = "405 - Not that way.<br /><br />We built a way for you to access the data.  Thanks.<br /><br />"
    msg += "  Let's <a href='https://ip2.themonkeyplayground.com'>start at the beginning</a> maybe."
    return msg

@app.errorhandler(500)
def page_not_found(e):
    msg = "500 - Who broke this?<br /><br />"
    msg += "  Let's try <a href='https://themonkeyplayground.com'>the main site.</a>  Is it working?  Okay, the app is broken."
    return msg