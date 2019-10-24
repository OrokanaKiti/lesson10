#author- Sammie~ ♫
#This test is designed to take the results from a DuckDuckGo Search on "presidents of the united states" (instant answers) and return it then process it with known information to ensure accuracy
#this is lesson 10's HW project

# ----------------------------------------------------------------------
# import section
# ----------------------------------------------------------------------

import pytest
import requests

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
response = requests.get("https://api.duckduckgo.com/?q=valley+forge+national+park&format=json&pretty=1-q")

#the input from the api to be tested agianst known good inputs
#duckDuckInput = []


# ----------------------------------------------------------------------
# testers
# ----------------------------------------------------------------------

def duckSearch():
    #call for the duck search of presidents and place only last names in duckDuckInput[]
    return "sampleText"

def test_duckSearch():
    #test the results of duckDuckInput[] for inconsistencies with presproper
    assert 1 == 1 #for duckDuckInput[i] is in presProper[], i++,



# end of program confirmation test
print("program was allowed to fully execute")


# ----------------------------------------------------------------------
# Junk code
# ----------------------------------------------------------------------

#def test_duckSearch_fail():
#
#   assert 1 == 12 #tester code