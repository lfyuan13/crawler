import os
import sys
from bs4 import BeautifulSoup as BS
import time


def extract_finance(content):
	try:	
		mySoup = BS(content)
		print 'mySoup'
		# para = {'charset': 'gbk'}
		# charset = mySoup.head.findAll('meta', para)
		# if charset is not None and len(charset)>0:
		# 	print charset
		# 	print 'gbk'
		# 	mySoup = BS(content.decode('gbk'))
		# else:
		# 	mySoup = BS(content.decode('utf8'))
		# 	print "utf8"

		para = {'property': 'og:type'}
		metaInfo = mySoup.head.findAll('meta', para)[0]
		print 'metaInfo'
		if metaInfo["content"]=='article':

			article_title = mySoup.body.findAll('h1', {'id':'artibodyTitle'})[0]
			
			article_info = BS(str(mySoup.body.findAll('div', {'class':'page-info'})[0]))
			article_datetime = article_info.findAll('span', {'class':'time-source'})[0]
			article_medianame = article_info.findAll('span', {'data-sudaclick':'media_name'})[0]

			article_body = BS(str(mySoup.body.findAll('div', {'id':'artibody'})[0]))

			# print format article
			print "title:", article_title.text.strip().encode('GBK')
			# print "datetime:", article_datetime.text.strip().encode('GBK')
			print "media_name:", article_medianame.text.strip().split()[0].encode('GBK')
			print "body:"
			ps = article_body.findAll('p')
			for p in ps:
				print p.text.strip().encode('GBK')
		else:
			print "no"
	except Exception as e:
		print e


def extract_content(content):
	try:	
		mySoup = BS(content)
		print 'mySoup'
		# para = {'charset': 'gbk'}
		# charset = mySoup.head.findAll('meta', para)
		# if charset is not None and len(charset)>0:
		# 	print charset
		# 	print 'gbk'
		# 	mySoup = BS(content.decode('gbk'))
		# else:
		# 	mySoup = BS(content.decode('utf8'))
		# 	print "utf8"

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
		else:
			print "no"
	except Exception as e:
		print e

file_dir = './data/'
n = 3
for parent, dirnames, filenames in os.walk(file_dir):	
	if 'finance' in parent or 'mil' in parent or 'sport' in parent:
		continue

	for filename in filenames:
		n-=1
		print filename
		f = open(os.path.join(parent,filename))
		if 'finance' in parent:
			extract_finance(f.read())
		else:
			extract_content(f.read())
		f.close()
		if n<0:
			sys.exit(0)
		
	
