#!/usr/bin/python3

"""versionupdate.py: modifies Chef environment files and replaces version"""
__author__      = "Carolyn Fischer"

import fileinput
import re
import sys
import linecache
import os
from conf import *

def change_version(repo_location, app_name, new_version, filename):
    os.chdir(repo_location)

    # check if the version is really a version for sanity check
    if not re.search("\d*.~\d*$", new_version):
        print("Version was not numerical and does match the pattern 1.1~123+, provided value was", new_version)
        sys.exit(1)

    if not re.match(r"([a-zA-Z\.-])*$", app_name):
        print("Application name is not alphabetical and does not match the patten [a-zA-Z.-]*, provided value was", app_name)
        sys.exit(1)

    # if all is given instead of file name, then loop over all files
    if "all" in filename:
        # copy environments tuple from conf.py
        filename = environments[:] 

    # loop over file(s).
    for env_file in filename:
        print("Processing file", env_file)

        # loop over all lines in the current file
        for current_line in fileinput.input(env_file):

            if app_name in current_line:
                #filter out false matches - no app name ends with a dot
                if app_name+'.' not in current_line:
                    #print("Found a match", current_line)
                    version_replace_line = fileinput.lineno() + 1

        if version_replace_line:
            #print("Found match on line", version_replace_line)
             pass
        else:
            print("Match not found!")
            sys.exit(1)

        #close the file, we got the line numbers and we're outta here           
        fileinput.close()

        # now that we have the line numbers, get the line to see if it contains version
        if version_replace_line:
            found_version_line = linecache.getline(env_file, version_replace_line)
#            print("found version line", found_version_line)
#            print("version replace line",version_replace_line)

            if ":version" in found_version_line:
                old_version = str(found_version_line.split("\"", 1)[1].split("\"", 1)[0])

                # open the file again to replace the version, can't do it in one run due to fileinput peculiarities
                for line in fileinput.input(env_file, inplace = 1):
                    if line == found_version_line:
                        exact_version_replaced = found_version_line.rstrip().replace(old_version, new_version)
                        print(exact_version_replaced)
                    else:
                        print(line.strip("\n"))

                print("Changing application", sys.argv[1])
                print("\tOld version is", old_version)
                print("\tNew version is", new_version)

                read_continue_answer = input("Do you want to continue [y]/n?\n")
                if read_continue_answer == "n":
                    sys.exit(0)
        else:
            print("Match was not found, exiting...")
            sys.exit(1)
