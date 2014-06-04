# -*- coding:utf-8 -*- 
from bs4 import BeautifulSoup as BS
import urllib
import sqlite3
import time


URL_NEWS = 'http://news.baidu.com/'
DB_NAME = "news.db"
TABLE_NAME = "news_tb"
SQL_INSERT = "insert into {0}(title, link, datetime) values('{1}', '{2}', '{3}')"  # table_name, title, link, datetime

db = sqlite3.connect(DB_NAME)
raw = urllib.urlopen(URL_NEWS).read()

if raw:
	soup = BS(raw)
	para = {
	    'class': 'ulist focuslistnews'
	}
	try:
		ul = soup.body.findAll('ul', para)
	    	for ul_item in ul:
			li = ul_item.li
			while li:
				temp = str(li)
				if temp.strip() == '':
					pass
				else:
					a = li.a
					sql = SQL_INSERT.format(TABLE_NAME, a.text.encode('utf-8'), a['href'].encode('utf-8'), time.ctime())
					db.execute(sql)
					print sql
				li = li.nextSibling
			print '==='*10
	except AttributeError:
		print "analysis error"
db.commit()
db.close()

