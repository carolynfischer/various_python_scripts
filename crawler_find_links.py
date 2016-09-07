#!/usr/bin/env python

sample_page = """<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Udacity</title>
</head>
<body>
<h1>Udacity</h1>
<p><b>Udacity</b> is a private institution of
<a href="http://www.wikipedia.org/wiki/Higher_education">higher education founded by</a> <a href="http://www.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike Sokolsky with the goal to provide university-level education that is "both high quality and low cost".</p>   
<p> It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Currently, Udacity is working on its second course on building a search engine. Udacity was announced at the 2012 <a href="http://www.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a> conference.</p>      
</body>
</html>"""

#print sample_page
loc = 0

while True:
    substr = sample_page.find('<a href="', loc)
    start = sample_page.find('"', substr)
    end = sample_page.find('">', start)
    loc = end + 1

    if start == -1 or end == -1:
        break
    else:
        print sample_page[start +1:end]
