#!/usr/bin/python3

"""git_handler.py: runs git pull, commits changes and pushes them out to master"""
__author__      = "Carolyn Fischer"

import sys
import os
from subprocess import call

def git_handler(repo_location, app_name, new_version, filename):
    os.chdir(repo_location)

    print("\nCommiting changes...")
    call("git commit -a -m 'Deployed new version "+ new_version + " of application " + sys.argv[1] + " to " + str(filename) + "'", shell = True)

    print("\nRunning git pull...")
    call("git pull --rebase", shell = True)

    print("\nRunning git push...")
    call("git push", shell = True)
