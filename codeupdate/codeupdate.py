#!/usr/bin/python3


"""codeupdate.py: main file which calls out the rest of the modules"""
__author__      = "Carolyn Fischer"

import re
import sys
import os
import git_handler
import versionupdate
import chef_update
from conf import *

if len(sys.argv) < 3:
    print("\tInvalid parameters. Usage: python codeupdate.py <app name> <new version> <env_file file>")
    sys.exit(1)

app_name = re.compile(sys.argv[1])
new_version = sys.argv[2]
filename = sys.argv[3:]

if __name__ == '__main__':

    selection = input("Select application type: \n1 stratus \n2 enter role name manually \n[1]: ").strip()
    if selection == "2":
        role_name = input("Enter role name: \n")
        print("Role name set to", role_name)
    else:
        role_name = "stratus-" + sys.argv[1].replace(".", "-")
        print("Role name is", role_name)

    print("Running version update on env files...")
    try:
        versionupdate.change_version(repo_location, sys.argv[1], new_version, filename)
    except IOError:
         print("\tCan\'t open file")
#    except NameError:
#         print("\tNameError was raised, local or global name is not found")
    except ValueError:
         print("\tIncorrect parameters")
    except TypeError:
         print("\tType mismatch")
    except RuntimeError:
        print("\tInvalid parameters. Usage: python codeupdate.py <app name> <new version> <env_file file>")

    try:
        git_handler.git_handler(repo_location, app_name, new_version, filename)
    except(RuntimeError):
        print("\tUnable to run")

    print("Role name is", role_name)

    if "all" in filename:
        chef_update.chef_update_all(repo_location, role_name)
    else:
        # Run chef for each env
        for env in filename:
            if "live" in env or "silent" in env:   
                environment = os.path.basename(env.split(".")[0])
                print(environment)

                try:
                    chef_update.chef_update(repo_location, role_name, environment, env)
                except(RuntimeError):
                    print("\tUnable to run Chef update")
            else:
                print(env + " is not a valid live environment")

sys.stderr.write('Finished processing\n')

