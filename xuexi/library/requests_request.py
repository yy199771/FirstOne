#coding=utf-8

import json
import requests
from requests import exceptions

URL = 'https://api.github.com'

def build_uri(endpoint):
    print 'test:' + '/'.join([URL, endpoint])
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def request_method():
    #response =requests.get('https://api.github.com/users/yy199771')
    response = requests.get(build_uri('users/yy199771'))
    #response = requests.get(build_uri('user/emails'), auth=('yy199771@163.com','******'))
    print response
    print better_print(response.text)

def params_requests():
    response = requests.get(build_uri('users'),params={'since':11})
    print better_print(response.text)
    print response.request.headers
    print response.url

def json_requests():
    response = requests.patch(build_uri('user'), auth=('yy199771','1qazxsw2'),json={'name':'yymmx'})
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code

def timeout_requests():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print response.text
        print response.status_code

def hard_requests():
    from requests import Request,Session
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('GET',build_uri('user/emails'), auth=('yy199771@163.com','1qazxsw2'),headers=headers)
    prepped = req.prepare()
    print prepped.body
    print prepped.headers

    resq = s.send(prepped, timeout=10)
    print resq.status_code
    print resq.request.headers
    print resq.text

if __name__ == '__main__':
    #request_method()
    params_requests()
    #json_requests()
    #timeout_requests()
    #hard_requests()