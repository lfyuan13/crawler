# -*- coding:utf-8 -*- 

'''
	crawl www.sina.com.cn news
'''

from bs4 import BeautifulSoup as BS
import urllib2
import sqlite3
import time


def GetDecodeContent(content):
	mySoup = BS(content)
	para = {'charset': 'gbk'}
	charset = mySoup.head.findAll('meta', para)
	if charset is not None and len(charset)>0:
		print charset
		print 'gbk'
		mySoup = BS(content.decode('gbk'))
	else:
		mySoup = BS(content.decode('utf8'))
		print "utf8"
	return mySoup

# url = "http://sports.sina.com.cn/others/athletics/2015-08-29/doc-ifxhkafe6173820.shtml"
url = "http://finance.sina.com.cn/"
path = 'data/sina/finance/'

result = []
fresult = open(path + 'result.txt', 'a+')
try:
	req = urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
	
	content = urllib2.urlopen(req).read()
	mySoup = BS(content)
	links = mySoup.findAll('a')
	print 'links:', len(links)

	links_tmp = []
	for link in links:
		try:
			if link['href'].endswith('html'):
				links_tmp.append(link['href']) 
		except Exception as e:
			print 'link error:', e
	links = links_tmp
	print 'crawl:', len(links), ' links'
	for link in links:
		time.sleep(15)
		print 'ok:', link
		sub_req = urllib2.Request(link)
		sub_req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
		article_content = urllib2.urlopen(sub_req).read()
		# article = GetDecodeContent(str(article_content))
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
	print "Exception:", e

for link in result:
	fresult.write(link + "\n")
fresult.close()

