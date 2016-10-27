#coding=utf-8
import requests

# 使用urllib
url_ip = 'http://127.0.0.1:8000/ip'
url_get = 'http://127.0.0.1:8000/get'

def use_simple_requests():
    response = requests.get(url_ip)
    print '>>>Response Headers:'
    print response.headers
    print '>>>Response body:'
    print response.text

def use_params_requests():
    params = ({'params1': 'hello', 'params2': 'world'})
    # 发送请求
    response = requests.get(url_get, params=params)
    # 处理响应
    print '>>>Response Headers:'
    print response.headers
    print '>>>Status Code:'
    print response.status_code
    print response.reason
    print '>>>Response body:'
    print response.json()

if __name__ == '__main__':
    #print '>>>Use simple request:'
    #use_simple_requests()
    print '>>>Use params request:'
    use_params_requests()
# 使用requests

