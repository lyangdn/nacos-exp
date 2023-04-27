# nacos-exp
Nacos身份绕过漏洞（QVD-2023-6271）EXP
使用方式：  
1、修改Authorization内的值为有效的JWT  
2、创建一个名为url.txt的文件，文件中放入你验证目标的url地址  
3、运行
4、存在漏洞的url存放在目录下的output.txt文件中，如存在output.txt，url会追加至文档最后  
使用代理方式  
将脚本中的proxy = 'http://127.0.0.1:3000'
前的#去掉，与proxies={"http": proxy, "https": proxy}前的#去掉即可  
支持ip:port形式  
运行截图  
![image](https://user-images.githubusercontent.com/95094405/234781612-534f171a-3ca5-435d-86d7-da9524eca25e.png)
