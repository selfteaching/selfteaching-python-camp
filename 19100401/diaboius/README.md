第一天学习的心得体会：
#第一，关于vscode的配置还是没有搞定；主要是终端无法启动，以及launch.json的配置问题；
#第二，关于克隆的思考，如果克隆对象发生了变化，还有重新克隆一次吗？有没有单独只克隆变化部分的办法；
#第三，关于克隆速度慢的问题初步解决
1、查询以下域名的IP地址，可以用 https://www.ipaddress.com/

    github.global.ssl.fastly.net
    github.com

2、把查询的得到IP 和对应域名放入系统 hosts下(这里需要管理员权限)

    151.101.184.249 github.global.ssl.fastly.net
    192.30.253.112 github.com
    192.30.253.113 github.com

3、刷新DNS

打开CMD 输入

ipconfig /flushdns

这个可以多来几次

然后再去克隆项目，速度从几十k 提升到几百k 甚至上m
--------------------- 
作者：bug开发 
来源：CSDN 
原文：https://blog.csdn.net/oZhangBi/article/details/82915994 
版权声明：本文为博主原创文章，转载请附上博文链接！
