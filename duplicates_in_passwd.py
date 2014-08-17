#!/opt/local/Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3
import re

file = open('/Users/carolyn/Documents/passwd')
data = []
for line in file:
	line = line.split(':')

	data.append(line[2])
	data.sort()



d = {}
for i in set(data):
	d[i] = data.count(i)
	if data.count(i) > 1:

		file.seek(0)
		for newline in file:
			newline = newline.split(':')
			if i in newline:
				print("Duplicate uid", i, "with username ", newline[0])
file.close()
