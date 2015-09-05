# -*- coding:utf-8 -*- 

'''
	crawl www.sina.com.cn news
'''

from bs4 import BeautifulSoup as BS
import urllib2
import sqlite3
import time

# url = "http://sports.sina.com.cn/others/athletics/2015-08-29/doc-ifxhkafe6173820.shtml"
url = "http://finance.sina.com.cn/china/bwdt/20150829/193023117100.shtml"

try:
	content = urllib2.urlopen(url).read()
	

	mySoup = BS(content)
	print 'mySoup'
	para = {'charset': 'gbk'}
	charset = mySoup.head.findAll('meta', para)
	if charset is not None and len(charset)>0:
		print charset
		print 'gbk'
		mySoup = BS(content.decode('gbk'))
	else:
		mySoup = BS(content.decode('utf8'))
		print "utf8"

	para = {'property': 'og:type'}
	metaInfo = mySoup.head.findAll('meta', para)[0]
	print 'metaInfo'
	if metaInfo["content"]=='article':
		article = BS(str(mySoup.body.findAll('div', {'class':'blkContainerSblk'})[0]))

		article_title = article.findAll('h1', {'id':'artibodyTitle'})[0]
		
		article_info = BS(str(article.findAll('div', {'class':'artInfo'})[0]))
		article_datetime = article_info.findAll('span', {'id':'pub_date'})[0]
		article_medianame = article_info.findAll('span', {'id':'media_name'})[0]

		article_body = BS(str(article.findAll('div', {'id':'artibody'})[0]))

		# print format article
		print "title:", article_title.text.strip().encode('GBK')
		print "datetime:", article_datetime.text.strip().encode('GBK')
		print "media_name:", article_medianame.text.strip().split()[0].encode('GBK')
		print "body:"
		ps = article_body.findAll('p')
		for p in ps:
			print p.text.strip().encode('GBK')

		fout = open(url.replace('/','_').replace(':','_'), 'w+')
		fout.write(content)
		fout.close()
	else:
		print "no"
except Exception as e:
	print e