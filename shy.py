#! /usr/bin/env python
# coding: utf-8
'''
douban 爬虫
2016-12-29

'''
__author__ = 'wymanqin'
import requests
import re
import os
from bs4 import BeautifulSoup
#解决ASCII码问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#2850
url = 'https://www.douban.com/group/haixiuzu/discussion?start=0'

user_agent 	= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
headers 	= { 'User-Agent' :  user_agent }
#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

content  	= requests.get(url, headers = headers)
pattern  	= re.compile('.*?<td class="title">.*?href="(.*?)" title="(.*?)".*?', re.S)
items 	 	= re.findall(pattern, content.text)
# 目录切换到下载图片的文件夹
os.chdir('/Users/wymanqin/group_shy/')
#f = open('shy.txt','w')
for item in items:
	item[0].encode('utf-8')
	item[1].encode('utf-8')
	print item[1] +'\n'
	print item[0] +'\n'	
	#f.write(item[1] +'\n')
	#f.write(item[0] +'\n')
	#进入详情页
	page_url = item[0]
	img_html = requests.get(page_url, headers = headers)
	pattern_pic = re.compile('<div class="topic-figure.*?<img src="(.*?)"', re.S)
	picurls = re.findall(pattern_pic, img_html.text)
	#print u'图片地址：',pics
	#download img
	for picurl in picurls:
		if picurl == None:
			print u'无图片 或者 不明原因'
		else:
			print u'图片地址： ', picurl
			name = picurl[-13: -4]
			img = requests.get(picurl, headers = headers)
			f = open(name +'.jpg', 'ab')
			f.write(img.content)
			f.close()


	
print u'--download finish--'











