# nacos-exp
Nacos身份绕过漏洞（QVD-2023-6271）EXP
使用方式：  
1、修改Authorization内的值为有效的JWT  
2、创建一个名为url.txt的文件，文件中放入你验证目标的url地址  
3、运行  
使用代理方式  
将脚本中的proxy = 'http://127.0.0.1:3000'前的#去掉，与proxies={"http": proxy, "https": proxy}前的#去掉即可  
