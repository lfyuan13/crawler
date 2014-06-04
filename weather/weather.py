# -*- coding:utf-8 -*-
"""
weather url:http://m.weather.com.cn/data/xxxxx.html
上面这个链接已经停止服务了，返回的天气都是2014.3.4
使用下面这个链接
http://m.weather.com.cn/atad/101230201.html
"""

import sys
import urllib as ul
import json
import time

sys.path.insert(0,'../')
import util

URL = "http://m.weather.com.cn/atad/{0}.html"
city_file = "data/city_code.txt"

city_dict = {}
with open(city_file) as f:
    for line in f:
        line = line.strip()
        if line == '':
            continue
        line = line.decode('utf-8')
        words = line.split()
        city_dict[words[0]] = words[1]


def get_by_city_name(city=u'北京'):
    if isinstance(city, dict):
        city = city['where']
    city = util.to_unicode(city)
    return get_by_city_code(city_dict[city])



def get_by_city_code(city_code='101110101'):
    """default city_code is 北京 """
    remote_url = URL.format(city_code)
    response = ul.urlopen(remote_url).read()
    response = util.to_unicode(response)
    
    try:
        data = json.loads(response)
        weather_info = data['weatherinfo']

        cur = get_current()
        temp = 'temp%d' % (cur)
        weather = 'weather%d' % (cur)

        re = {
            'date' : weather_info['date_y'],
            'city' : weather_info['city'],
            'temp' : weather_info[temp],
            'weather' : weather_info[weather],
            'tip' : weather_info['index_d']
        }
    except ValueError:
        re = None
    return re

def get_current():
    t = time.localtime().tm_hour
    if t>=8 and t<14:
        return 1
    if t>=14 and t<20:
        return 2
    if t>=20 and t<2:
        return 3
    if t>=2 and t<8:
        return 4
    else:
        return 1

def test(city):
    re = get_by_city_name(city)
    print city
    if re:
        for k in re:
            print k, ':', re[k]
    else:
        print 'catch none'

if __name__ == '__main__':
    test('连城')
    test('北京')
    test('上海')
