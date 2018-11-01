# SeniorDesign

Files that can be used to run VERA, save location to home directory, and text user when finished.

Files that go to directory on your local machine (desktop, laptop, etc.):
runmpact.sh

Files that go to directory on server:
core_run.sh,
run_checker.py

Setup
1.  Put files in correct spots as listed above
2.  In core.sh file the first line is the simulation name to run, change it to what is needed
    Second line is number of computer cores to be used, change it accordingly
    The last line copies the files to a specific location, change it accordingly
3.  In runmpact.sh file change username accordingly and comment out texting section if needed
4.  If using texting file, will require account with Twilio and changing authentication key etc.

To run script from server:
1. Put "core_name".inp file in same directory as core_run.sh file
2. execute:  bash core_run.sh &
   This will run in background so you can leave the server and program will still run
   Leave off the & symbol if you don't want to run in background
