#coding='utf-8'

import json
import requests

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

if __name__ == '__main__':
    request_method()