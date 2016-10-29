#coding=utf-8

import requests

def download_image():
    url = 'http://img3.imgtn.bdimg.com/it/u=2518419245,374265958&fm=21&gp=0.jpg'

    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    response = requests.get(url, headers=headers, stream=True)

    print response.status_code
    print response.headers

    # 流模式,此时流模式并未关闭
    with open('demo.jpg','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


def download_image_improved():
    # 伪造headers信息:
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

    # 限定URL
    url = 'http://img3.imgtn.bdimg.com/it/u=2518419245,374265958&fm=21&gp=0.jpg'
    response = requests.get(url, headers=headers, stream=True)

    from contextlib import closing
    # 增加一个上下文传递
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        # 打开文件
        with open('demo.jpg','wb') as fd:
            # 每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


if __name__ == '__main__':
    #download_image()
    download_image_improved()