# -*- coding:utf-8 -*-
import random
import time
import requests

def getHeaders():
  uaList=[
    'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+GTB7.1;+.NET+CLR+2.0.50727)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 712 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
  ]

  headers = {
              'Host': 'xxxxxxxxxx', 
              'User-Agent': random.choice(uaList)
            }

  return headers

def saveFile(filepath, url):
  headers = getHeaders()

  print('Start from the website...')
  start = time.time()

  response = requests.get(url, headers=headers, stream=True) #stream=True必须写上

  size = 0    #初始化已下载大小
  chunk_size = 1024  # 每次下载的数据大小
  content_size = int(response.headers['content-length'])  # 下载文件总大小

  with open(filepath, 'wb') as f:
    for data in response.iter_content(chunk_size = chunk_size):
      f.write(data)
      size +=len(data)
      print('\r'+'[下载进度]:%s%.2f%%' % ('||'*int(size*50/ content_size), float(size / content_size * 100)) ,end=' ')


if __name__ == '__main__':
  url = 'xxxxxxxxx'
  saveFile('xxxxx',url)

