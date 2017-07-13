# Nimble Storage Coding Challenge
Python script that will read debug*.log files

To run the script, type:
	* "python3 analyze_log.py --file ./debug\* --pattern (pattern)""
The two patterns tested for this coding challenge are:
	* "vol-test-111"
	* "vol-test-222"

Problems:
    1. Can only handle one user input (maybe make sys.argv[n]?)
    2. Traceback doesn't work
        * need to find a way to find line number (lineNum)
        What I was thinking to impliment the code:
        * use lineNum+2 to find timestamp
        * if timestamp does not exist, do not print to output
        * if timestamp exist, then ...
        * search if searchName is in Traceback lines
        * if searchName is not found, do not print to output file
        * if searchName is found, print from Traceback line to timestamp line to output file
        * to print print this, use the i-(lineNum+2) to get total lines needed
        * use for loop with range of total lines needed to print to output file
    3. In calling the script, "python3 analyze_log.py --file ./debug* --pattern vol-test-111", the script will "not --file"
        * to make this work use "python3 analyze_log.py --file ./debug\* --pattern vol-test-111"

        
Confusion with coding:
    1. There was no "'severity': 'error'" in the debug*.log files so I guess how to implement them into the script
    	* output.txt will display searched lines if ""'severity': 'error'" in line" are removed where seen in code
    2. For the Traceback condition, I'm not entirely sure where to stop seaching the searchName