#!/usr/bin/env python
import fileinput

filename = '/etc/passwd'

'''
def count(filename):
    occurrences = 0
    for line in fileinput.input(filename):
        line = line.split(":")
        username = line[0]
        return username

print(count.username)
'''

for line in fileinput.input(filename):

    field = line.split(":")
        #dictionary = {field.split(":")[0]: field.split(":")[2]}
    print(field[0])
        #print(dictionary)