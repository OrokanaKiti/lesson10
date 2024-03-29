#author- Sammie~ ♫
#This test is designed to take the results from a DuckDuckGo Search on "presidents of the united states" (instant answers) and return it then process it with known information to ensure accuracy
#this is lesson 10's HW project

#Authors commentary During development---------------------------------------------------------
# NOTE Finding a Instant search displaying all the presidents is taking up lots of time
# NOTE "The program for the Lesson 10 lab on Integration tests and the REST api has been changed.  It now involves verifying Presidents of the US being listed on the White House website." Check this! We might not need DDG
# NOTE for self later http://www.gregreda.com/2015/02/15/web-scraping-finding-the-api/ Might be useful to webscrape the data from a simple site
# NOTE Attempting to webscrape from this site wish me luck https://www.presidentsusa.net/presvplist.html also a git hub with a similar concept https://github.com/hitch17/sample-data/blob/master/presidents.json
# NOTE JSON FOUND THAT IS USABLE https://github.com/hitch17/sample-data/blob/master/presidents.json HAS A JSON FILE (INCORRECT DATA)
# LASTMINUTE time is getting short- too little time to continue to follow a pipe dream.. i NEED a json file to work with
# LASTMIUTE creating a Json File with all the data i needm, importing it as a var and then using IT to push my tests
# NOTE according to teacher it is still positive to find the  https://api.duckduckgo.com/?q=Presidents+of+the+United+States&format=json&pretty=1 like i intiialy tried with no result.. trying teachers advice  ; w ; im so short on time
# Note There is so much Data to parse in the provided json file..  there arnt even clear places to take the data- might just scan the whole site for the mention of the stated list.. if a word is missing that should call error

# ----------------------------------------------------------------------
# import section
# ----------------------------------------------------------------------

import pytest
import requests
import json
#import BigSmiles
#import WholesomeStuff!!!!


# ----------------------------------------------------------------------
# var section of the code
# ----------------------------------------------------------------------


#this is a list of known good inputs to test agianst
presProper = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln",
                  "Johnson", "Grant" , "Hayes", "Garfield" , "Arthur", "Cleveland" , "Harrison", "Cleveland" , "McKinley", "Roosevelt" , "Taft", "Wilson" , "Harding", "Coolidge" , "Hoover",
                  "Roosevelt" , "Truman", "Eisenhower" , "Kennedy", "Johnson" , "Nixon", "Ford" , "Carter", "Reagan" , "Bush", "Clinton" , "Bush", "Obama" , "Trump"]
#sample inputs used in inital testing or editing in the code
sample_input_good = ["Adams"]
sample_input_bad = ["JoeMama"]
response = requests.get("https://api.duckduckgo.com/?q=Presidents+of+the+United+States&format=json&pretty=1")


#the input from the api to be tested agianst known good inputs
#duckDuckInput = []


# ----------------------------------------------------------------------
# testers
# ----------------------------------------------------------------------

def  jsonSearch(JSON):
    #call for the duck search of presidents and place only last names in duckDuckInput[]
    #WIP SEARCH FEATURE OUT OF SCOPE
    return "sampleText"

#PYTEST WIP
def test_duckSearch(JSON):
    content = json.dump(JSON, JSON["Text"])
#    #test the results of response for inconsistencies with presproper
    #need to search the json file for the 'Text' Key, then validate that at least one 'Text' key has the value of the last name mentioned at least once

    assert 1 == 1 #for duckDuckInput[i] is in presProper[], i++, #Default assert until ready to enter proper search

def jprint(obj):
    #testing code to learn how to parse a JSON input from a API system #it seems dumps allows a program to convert and work with the json data
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# ----------------------------------------------------------------------
# Testing Main
# ----------------------------------------------------------------------

print(response.status_code) #for ackowledging any issues
#print(response.json())
#jprint(response.json()) #TEST CODE for checking material
json.dump(response, response["Text"])
#jsonSearch(response)

# end of program confirmation test
print("program was allowed to fully execute")

# ----------------------------------------------------------------------
# Junk code
# ----------------------------------------------------------------------
#import my_attempt_to_make_you_happie_~♫


#def test_duckSearch_fail():
#
#   assert 1 == 12 #tester code

#
## File attmempt to scan data gathered from a site   *****CANCELLED DUE TO TEACHER INTERVENTION********
#with open('data.txt') as json_file:
#    data = json.load(json_file)
 #   for p in data['people']:
 #       print('Name: ' + p['name'])
#
#
##print(response['Result'])
#

#
# USED TO TEST OR ATTEMPT TO LOOP THRU A JSON FILE to search for general content
#    for key in J:
#            value = J[key]
 #           print("TEST TEST SAAMPLE ({}) = ({})".format(key, value))
#
#
#
#

# ----------------------------------------------------------------------
# Notes Learned
# ----------------------------------------------------------------------
# Json Dumps is a conversion from java script to workable Strings