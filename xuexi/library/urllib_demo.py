#coding=utf-8
import urllib2
import urllib

# 使用urllib
url_ip = 'http://www.we.com/'
url_get = 'http://www.we.com/fund/info/tag000001'

def use_simple_urllib2():
    response = urllib2.urlopen(url_ip)
    print '>>>Response Headers:'
    print response.info()
    print '>>>Response body:'
    #print ''.join([line for line in response.readlines()])

def use_params_urllib2():
    # 构建请求参数
    params = urllib.urlencode({'params1':'hello','params2':'world'})
    print '>>>Request Params:'
    print params
    # 发送请求
    response = urllib2.urlopen('?'.join([url_get, '%s']) % params)
    # 处理响应
    print '>>>Response Headers:'
    print response.info()
    print '>>>Status Code:'
    print response.getcode()
    print '>>>Response body:'
    print ''.join([line for line in response.readlines()])

if __name__ == '__main__':
    #print '>>>Use simple urllib2:'
    #use_simple_urllib2()
    print '>>>Use params urllib2:'
    use_params_urllib2()
# 使用requests

