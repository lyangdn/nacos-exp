# nacos-exp
Nacos身份绕过漏洞（QVD-2023-6271）EXP
使用方式：  
1、在脚本目录下创建一个名为JWT.txt的文件，在JWT.txt文件中写入构造好的JWT  
2、创建一个名为url.txt的文件，文件中放入你验证目标的url地址  
3、运行  
4、存在漏洞的url存放在目录下的output.txt文件中，如存在output.txt，url会追加至文档最后  
使用代理方式  
在询问是否使用代理中输入y  
输入代理的端口号，默认是使用本机代理端口，如果使用隧道代理请修改源码  
支持ip:port形式  
运行截图  
![image](https://user-images.githubusercontent.com/95094405/234781612-534f171a-3ca5-435d-86d7-da9524eca25e.png)
