#!/usr/bin/python
#coding:utf-8

import urllib2
import re
import urllib

#获取网页的HTML
def get_html(url):
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	html=response.read()
	return html

def get_image(html):
	pattern=r'src="(.+\.jpg)"'
	image=re.compile(pattern)
	image_list=re.findall(image,html)
	index=0

	for line in image_list:
		urllib.urlretrieve(line,'%d.jpg' % index)
		index+=1

#------------------test---------------------
html=get_html("http://python.jobbole.com/81336/")
get_image(html)
#print html

