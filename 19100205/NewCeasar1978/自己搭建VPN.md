# 自己搭建VPN

自己搭建了一个VPN，其实中间有很多东西都不是特别清楚，也还在慢慢学习和完善。我就先给出一个实现翻墙的步骤，翻墙之后可以看到很多自己搭建VPN的方法，进一步的内容可以一起探索

简单来说自建 VPN 基本三步解决：

* 租一个虚拟服务器（VPS）

* 配置shadowsocks
* 下载SS或者SSR客户端，连接外网

另外可以搞一个Google BBR，翻墙速度快好多



## 租一个虚拟服务器

这一步比较简单，找一个靠谱的地方租一个虚拟服务器即可。推荐比较多的是[valtr](https://my.vultr.com/)，过程简单粗暴注册 -> 充值 -> 购买服务器即可，最便宜的貌似是$2.5/月，我用的是$5/月

* server location : 机房的位置，可以自己选择。我用的Los Angeles
* Server Type : 是虚拟的操作系统类型，我看大部分选择的是CentOS，不是很明确原因自己选的也是这个
* Server Size : 自己评估了一下，基本最低版本够用。看自己的需求
* Additional Features : 我选择前两个，第一个是IP协议，第二个是自动备份功能。我觉得第二个应该用得上还在研究中
* Startup Script、SSH Keys 空着就好
* Server Hostname & Label : 服务器的名字，不高兴也可以空着

最后点击 Deploy Now 就购买完成了，之后会自动跳到 VPS 列表页，status这个时候显示的installing，这是在安装操作系统，等它显示为runing后就完成



## 配置shadowsocks

这个时候点击status后面的更多图标，出现会出现浮图层，选择 View Console 进入命令窗口配置

* 身份验证：

  > * 点击原网页中OS下面的图标，会进入Server Information 界面，里面有 Username 和 Password
  > * 在命令窗口中输入 Username（回车），之后会显示 Password 输入提示，输入Password即可。需要注意的是这里和之前14天训练营中 Password 的输入有些类似，光标是不会移动的，输入即可
  > * 验证成功之后会出现[root@服务器名~]#的字样，就可以进入下一步

* 安装shadowsocks :

  > * 输入：`wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowcks.sh` （回车）
  > * 成功之后会出现[root@服务器名~]#的字样，就可以进入下一步

* 设置shadowsocks的执行权限：

  > * chmod +x shadowsocks.sh （回车）
  > * 成功之后会出现[root@服务器名~]#的字样，就可以进入下一步

* 配置 shadowsocks：

  > * shadowsocks.sh 2 >& 1 | tee shadowsocks.log （回车）
  > * 中间会提示输入 ERVER 的账号和端口。我表示没有看懂，就一路回车了，反正不输入就是默认。出现确认提示的时候 输入 y 后，回车即可
  > * 安装完成后会出现 shadowsocks 的信息并且标红了。这个一定要复制下来以备后用



## 下载SS或者SSR客户端，连接外网

* 下载一个 SS 或者SSR 的客户端，安装完成后，打开服务器设定，添加服务器。

* 输入上一步最后复制下来的内容（地址、端口、加密方式、密码等）

* 最后打开自动代理模式或者全局代理模式即可



关于Google BBR 加速，有一个问题就是需要准备即更换 centOS 7 的内核。具体内容参考[这个链接](https://zhuanlan.zhihu.com/p/62257675)