# -*- coding:utf-8 -*- 

'''
	crawl www.sina.com.cn news
'''

from bs4 import BeautifulSoup as BS
import urllib2
import sqlite3
import time

# url = "http://sports.sina.com.cn/others/athletics/2015-08-29/doc-ifxhkafe6173820.shtml"
host = "sports.sina.com.cn"
url = "http://sports.sina.com.cn/"

path = 'data/sina/sport/'
result = []
fresult = open(path + 'result.txt', 'a+')
try:
	req = urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
	# req.add_header('Host', host)
	content = urllib2.urlopen(req).read()
	mySoup = BS(content)
	links = mySoup.findAll('a')
	links = [link['href'] for link in links if link['href'].endswith('html')]
	print 'crawl:', len(links), ' links'
	for link in links:
		time.sleep(3)
		print 'ok:', link
		sub_req = urllib2.Request(link)
		sub_req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
		article_content = urllib2.urlopen(sub_req).read()
		article = BS(str(article_content))
		para = {'property': 'og:type'}
		if article:
			try:
				metaInfo = article.head.findAll('meta', para)
				if metaInfo is not None and len(metaInfo)>0 and metaInfo[0]["content"]=='article':
					print 'article:', link
					filename = link.replace('/','_').replace(':','_')
					fout = open(path + filename + '.txt', 'a+')
					fout.write(article_content)
					fout.close()
					print 'save ok...'
			except Exception as e:
				result.append(link)
				print 'Error:', e

except Exception as e:
	print e

for link in result:
	fresult.write(link + "\n")
fresult.close()

