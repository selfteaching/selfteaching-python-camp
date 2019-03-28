# Day 11
首先今天做的东西很好玩，感觉有点爬虫技术的意思。之前和大佬聊天，某大佬和我说过大概思路，就是用python去网页上爬取信息，然后发到邮箱里通知自己。可以爬天气预报或者是不定期发布的公告等。

第一个库requests  就是从网站上获取信息，这个看一下例子直接用给的get方法通过url就可以获得网页的基本信息，顺利完成今天的任务。大概看了一下，当然还有post、head等这些HTML的方法。
这样获得的是一个完整的HTML，print一下也可以看到他由完整的<title><head><body>。试了一下他别的方法，比如可以看当前的处理状态，比如200（正常完成）。

通过request获得网页返回结果后，开始对网页信息进行抓取，提取那些我们感兴趣的内容。
这里使用pyquery库，我直接安装pyquery库，import的时候看到使用的，但是运行的时候却提示找不到模块，搜了一下，发现要装一个lxml的库，这个最好是去网站上找，选择与自己目前使用python匹配的版本下载（复习：在vs code左下的状态栏可以看到目前的python版本）。然后装这个库，but这个下载的东西要放在运行的目录下（我是user\admin），装完这个库，再回去运行pyquery就可以了。没装pyquery还是要装啊。
关于抓取代码文档直接给出来了，没有什么坑，主要是理解意思：document=response.text,应该就是之抓取文字信息，content = document("#js_content").text(),把抓取的内容写成可视的文字，#js_content可能是某种格式转换（这个我没太想清楚，还拜托大家解惑），总之看文档它要和前面变量是一个名字。

调前两天的分词模块没什么问题，可是要把结果转成字符串以方便发送邮件。要相对函数结果进行操作，函数就必修有返回值，这里让stats_text返回两个函数就可以了，只不过一开始我没有给返回函数写参数，于是一直出现结果不太对的情况。即便是返回函数，改写的参数也要写上！ 另外python对于函数的返回要求并不严格，不写返回值也没什么事（只要你调用也没有用到），像C没有返回也必须写个void，所以在定义函数的时候容易忘记不写返回，最好养成习惯函数末尾都加一个return。

然后就是让我花费时间最多的发邮件这一部分
今天用的是yagmail(yet another gmail)，然后去网页上搜的话出来的基本上都是用smtplib这个库的。
一点点说吧。。。
首先提示说gmail不能用就是不能用，不是翻个墙那么简单的事。虽然翻墙在网页上操作可以发（这个我试过了），但是用python就是连接不上，可能和服务器有关系，总之还是用别的邮箱吧。
我发邮件用的是163邮箱，然后用另外一个qq邮箱测试

关于保护隐私，文档里也说了，用getpass，因为代码是要公开的，所以不要直接在参数里写

然后就是各种连接不上，连接超时啊，10060这个TCP连接失败啊。
于是我就开始了长达不知道几个小时的各种尝试

直接说结果吧，设置163smtp服务的时候他让你输入了一个授权码，然后短信验证的时候还有一个号码，当时网页上弹出来是将这两个号码绑定验证的，所以我试的时候就一直用这两个号码。
然而正确的操作并不是。用户名还是输入你的邮箱就是xxx@163.com，密码输入你的这个授权码。
之后再SMTP的参数里，多输入一个参数，就是smtp服务器，告诉他应该用哪个服务器，比如我是smtp.163.com，不输这个参数也连接不上（这个是我摸索了各种问题，中间还出现了SSL版本错误的这种神奇操作）

然后就可以顺利的发邮件啦，除了格式不大美观，可是超快超迅速啊！

整体感受就是，调试不要放弃啊，试着试着正解就突然出现了啊！还有就是知识知道的越多解决问题的时候就更加从容一些。我之前学过一点通信的知识，所以今天一方面属于上手实验了，还有一方面看到他报的一些错误，心里也知道他是怎么一回事，不是致命错误也不慌。
不要放弃学习啊！！！之前我选那个课老师上的是一言难尽，很多同学都放弃治疗了，然而还是要考试啊，最后不得不跑到图书馆借了本通讯原理看。今天发现没白看呀！







# Day 2
**首先是安装anaconda、jupyter lab、VS code**

![](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/002.3.png)![](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/002.4.png)

- vs code中添加代码时，要记得为上一行补上逗号 *否则会报错*
![](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/002.5.png)

状态栏显示

![](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/002.6.png)

在VScode中打开终端

![](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/002.7.png)

### Jupyter lab中并没有显示书的完整文件的解决办法 
一开始我打开jupyter lab，里面并没有克隆的文件夹，只能手动一个个upload，但是我觉得肯定不是这样的，后来经过猜测与验证发现：
如果克隆的位置不是操作的位置，则打开jupyter lab时是不会显示文件的
解决办法就是：
手动将克隆下来的文件添加到操作的位置即可
比如 我的位置时c:\user\admin（打开jupyter lab也只显示我admin中有的文件）
而我克隆仓库的位置是d盘，所以我将那个文件夹考到admin中，再启动jupyter lab，
就可以看到一本完整的书的文件夹了。
还有一种办法就是每次手动cd你克隆的位置，然后再jupyter lab
最后就可以流畅方便的阅读了

![](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/002.1.png)

### VSCode 中混杂有中文的解决办法 
一开始我的vs code中混有英文，比如搜索命令的时候还有编译时候的提示，这导致和教程上内容存在一定差异，以及阅读学习的不流畅，如果出现有相同问题的同学可以参考这个办法。
就是点左侧最下面一个按钮，然后输入“english”

最上面的应该是english support for languagetool,他的右下角有一个绿色的install(这恰恰表示还未安装)，于是点击install
重新启动vs code
这次就是全英的界面了


# Day 1
### 1.在Github中直接添加文件，进入要编辑的branch,如图点击create new file
![](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/001.1.png)
### 2.下载使用Sourcetree
  - **时涉及到bitbucket的注册验证，可能由于是国外的网站，响应特别慢（可能存在着刷不出来的风险），于是直接开了加速器，顺利下载安装**
![下载完成](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/001.2.png)
  - **使用URL进行克隆**
![使用URL进行克隆](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/001.3.png)
  - **克隆结果**
![](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/001.4.png)
  - **默认自动语言是中文，为了统一我修改了语言，English看着更舒服**
![](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/001.5.png)
  - **在本地仓库创建文件,采用了手动上传的方法，sourcetree中也能够同步显示**
![](https://github.com/slona-song/selfteaching-python-camp/blob/master/19100105/slona-song/image/001.6.png)
