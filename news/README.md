改目录下的是抓取新闻，
功能将要实现
（1）抓取最新的综合类新闻
（2）抓取最新的各类新闻：国际，军事，体育，互联网，娱乐，财经等


1、新浪
新浪的文章节点都有共性：体育
<head>节点下的
	<meta name="keywords" content="xx,xx,xx">  表示关键字
	<meta property="og:type" content="article"> 表示是文章类型
</head>

<body>下文章：
	<div class="blkContainerSblk">
		<h1 id="artibodyTitle"/>
		<div class="artInfo">
			<span id="pub_date" />
			<span id="media_name" />
		</div>
		<div class="BSHARE_POP" id="artibody">
			<p></p>
		</div>
	</div>
</body>

编码问题：
para = {'charset': 'gbk'}
	charset = mySoup.head.findAll('meta', para)
	if charset is not None and len(charset)>0:
		print charset
		print 'gbk'
		mySoup = BS(content.decode('gbk'))
	else:
		mySoup = BS(content.decode('utf8'))
		print "utf8"

2、百度新闻 
<div class="bd">
在<ul><li>里面
<a href="http://zhanglei.baijia.baidu.com/article/152196" target="_blank" mon="ct=1&amp;a=1&amp;c=internet&amp;pn=1">锤粉：真的猛士敢于在说完相声后直面惨淡的人生</a>



<meta http-equiv="newbaijia" content="newbaijia">

(1)如果是用的铁血网http://bbs.tiexue.net/post2_9425309_1.html
<div class="main" id="main">
<h1 class="post_tit">美剧中F-18舰载机大战中巴枭龙战机</h1>
<p/>
$('#main p')


(2)前沿网http://hot.qianyan001.com/20150830/114476_1.html








