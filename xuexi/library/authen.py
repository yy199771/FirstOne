#coding=utf-8

import requests

BaseUrl= 'https://api.github.com'

def construct_url(end_point):
    return '/'.join([BaseUrl, end_point])

def basic_auth():
    '''基本认证
    '''

    response = requests.get(construct_url('user'),auth=('yy199771@163.com',''))

    print response.text
    #print response.json()
    print response.request.headers

def basic_oauth():
    headers = {'Authorization':'token 4bcec94b701254e7cc70023c519e0da42ba9d9c6'}
    # user/emails
    response = requests.get(construct_url('user/emails'), headers=headers)
    print response.request.headers
    print response.text
    print response.status_code

from requests.auth import AuthBase

class GithubAuth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        # requests 加headers
        r.headers['Authorization'] = ''.join(['token', self.token])
        return r

def oauth_advanced():
    auth = GithubAuth('4bcec94b701254e7cc70023c519e0da42ba9d9c6')
    response = requests.get(construct_url('user/emails'), auth=auth)
    print auth.token
    print construct_url('user/emails')
    print response.text


if __name__ == '__main__':
    #basic_auth()
    #basic_oauth()
    oauth_advanced()