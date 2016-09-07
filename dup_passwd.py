#!/usr/bin/python2

ids = {}

with open('passwd') as f:
    for line in f:
        # get even elements and then get the first two
        name, id = line.split(":")[0::2][:2]
        if id not in ids.keys():
            ids[id] = []
        ids[id].append(name)

print ids

for k, v in enumerate(ids):
    if len(ids[v]) > 1:
        print v, ids[v]
