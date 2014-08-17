#!/usr/bin/python3

import os

#Chef environments file location
home = os.environ['HOME']
repo_location=os.getenv('HOME') + "/path/to/environment/files/"
print(repo_location)
#executable location that changes your environment in knife.rb to live
chef_environment="/usr/bin/livechef"
environments = ( 'prodenv1.rb', 'prodenv2.rb', 'prodenv3.rb', 'prodenv4.rb' )
