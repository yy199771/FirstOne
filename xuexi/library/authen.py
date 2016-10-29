#coding=utf-8

import requests

BaseUrl= 'https://api.github.com'

def construct_url(end_point):
    return '/'.join([BaseUrl, end_point])

def basic_auth():
    '''基本认证
    '''

    response = requests.get(construct_url('user'),auth=('yy199771@163.com','1qazxsw2'))

    print response.text
    #print response.json()
    print response.request.headers


if __name__ == '__main__':
    basic_auth()