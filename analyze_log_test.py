# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 05:58:32 2017

@author: imbko
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

Nimble Storage Coding Challenge
Bryan Ko (bkko@ucsc.edu)

Thank you for giving me the opportunity to do this coding challenge. Here is some documentation of the issues with the script.

Problems:
    1) Can only handle one user input (can be fixed if made into def)
    2) Traceback doesn't work
        - need to find a way to find line number (lineNum)
        What I was thinking to impliment the code:
        - use lineNum+2 to find timestamp
        - search if searchName is in Traceback lines
        - if searchName is not found, do not print to output file
        - if searchName is found, print from Traceback line to timestamp line to output file
        - to print print this, use the i-(lineNum+2) to get total lines needed
        - use for loop with range of total lines needed to print to output file
    3) In calling the script, "python3 analyze_log.py --file ./debug* --pattern vol-test-111", the script will "not --file"
        - not sure why, but it has something to do with * (will not affect the script)

        
Confusion with coding:
    1) There was no "'severity': 'error'" in the debug*.log files so I guess how to implement them into the script
    2) For the Traceback condition, I'm not entirely sure where to stop seaching the searchName
"""
import glob, sys

#reads --file
userFiles = sys.argv[1]
#reads file
fileName = sys.argv[2]
#reads --patter
userSearch = sys.argv[3]
#reads a search input
searchName = sys.argv[4]

#will not stop script if typed wrong since these are not bounded to anything
if userFiles != "--file":
    print("not --file")
if userSearch != "--pattern":
    print("not --pattern")

#read files in current dir starting with debug and ending with .log
debugFiles = glob.glob(fileName+'.log')

output = open('output_test_' + searchName + '.txt', 'w')
#for loop to cycle through all the files sorted by the glob.glob
for file_name in debugFiles:
    #check what files are read
    #print(file_name)
    with open(file_name, 'r') as f:
        searchlines = f.readlines()
        for i, line in enumerate(searchlines):
            #output lines starting with 'request' and contains user input and 'severity': 'error'
            if line.startswith('request') and searchName in line:
                output.write(line)
            #output lines starting with 'response' and contains user input and 'severity': 'error'   
            if line.startswith('response'):
                for lines in searchlines[i:i+3]:
                    #check if the output is correct
                    #output.write(lines)
                    if searchName in lines:
                        for j in range(3):
                            output.write(searchlines[i+j])
            #output lines starting with 'Traceback' and contains user input and
            #Traceback does not work.
#            if line.startswith('Traceback'):
#                for lines in searchlines[i:i+25]:          #not sure how many lines are needed after Traceback is found
#                    if lines.startswith('Exception:'):     #after Exception: two lines under should be the timestamp
#                        print(lines)                       #this is where I wanted to get lineNum, but could not find how to do it
                                                            #with lineNum, I will be able to get all the lines needed to write to output
                                                            #an issue I may encounter is where to stop searching for the searchName
    """
    #check if file actually reads the debug1.log
    f = open(file_name, 'r')
    output = open("debug2.txt","w")
    output.write(f.read())
    output.close()
    f.close()
    """
    output.close

"""
#print debug logs to text file for readability for me
fdebug = open("debug1.log","r")
fdebugtxt = open("debug1.txt","w")
fdebugtxt.write(fdebug.read())
fdebugtxt.close()
fdebug.close()
"""