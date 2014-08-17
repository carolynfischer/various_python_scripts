#!/usr/bin/python3


"""chef_update.py: manages environment upload and update of chef nodes"""
__author__      = "Carolyn Fischer"

import sys
import subprocess
import os
from conf import *

def chef_update_all(repo_location, role_name):
    """ Upload all live environment files to chef server  """

    os.chdir(repo_location)
    subprocess.call(chef_environment, shell = True)

    # environments are defined in conf.py, a list of chef environment files
    for env in environments:
        print("Uploading ", env)
        subprocess.call("knife environment from file " + env, shell = True)

    subprocess.call("knife ssh role:" + role_name + " 'sudo chef-client'", shell = True)

def chef_update(repo_location, role_name, environment, env):
    """ Upload individual environment files """
    
    os.chdir(repo_location)

    selected_node = subprocess.Popen(["knife search node 'role:" + role_name + " AND environment:" + environment + "' |grep 'IP'|head -1|awk {'print $2'}"], shell=True, stdout=subprocess.PIPE)

    output = str(selected_node.communicate()[0].strip(), "utf-8")

    print("A random node from the pool:", output)
    print("Uploading chef environment ", environment)

    subprocess.call("knife environment from file " + env, shell = True)
    knife_ssh_answer = input("Would you like to continue with knife ssh [y]/n?")

    if knife_ssh_answer == "n":
        print("You chose not to continue, exiting")
        sys.exit(0)
    else:
        which_run = input("Would you like to run it in \n1)" + output + "\n2)" + environment + "\n[1]/2? \n")
        if which_run == "2":
            print("\nRunning chef on role " +  role_name + " and environment " + environment)
            subprocess.call("knife ssh 'role:" + role_name + " AND environment:" + environment + "' 'sudo chef-client'", shell = True)
        else:
            print("Running chef-client on ", output)
            subprocess.call("ssh " + output + " 'hostname; sudo chef-client'", shell = True)
