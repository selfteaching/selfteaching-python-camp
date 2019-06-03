day1
昨天安装好了GitHub Desktop，Anaconda，VSC,
用Anaconda Prompt拉起来Jupyter lab但还并不知道干嘛用。
本来想用Jupyter notebook获得更好阅读体验，结果Win系统卡在了用toc插件将 ipynb 文件中的标题转换成目录这步。
今天学习了branch，commit,pull request和merge，issue的简单操作
Clone了repository到本地，新建立了Hello World repository
英文基本没有障碍，添加了一些编程语境比如branch, commit, default, push, origin, sprint etc.
遗留问题：作业最后一项在本地新建文件，README.md和 1001S02E01_helloworld.txt 是用改文件后缀方法建立的，
初始格式选的txt，发现在公共作业库里显示的是 Create 1001S02E01_helloworld.txt.txt 双后缀，不知道做的对不对。等教练反馈啦

day2
学号：1901050028
姓名：Hailey
学习内容：配置本地运⾏开发环境
学习用时：4.5h
收获总结： 
️Anaconda，VScode, Jupyter Notebook准备工作时已经安装好了，节约了时间。
️在VScode里配置python环境费了些时间，链接默认下载的适用于win32位。安装时没有发现，导致在VScode里配置python环境时没法自动检测到，卸载重装了64位之后问题解决。
️安装VScode内python扩展插件也比较顺利。
️Hello World编写运行比较容易，但是Hello World就是单词书里的abandon！每次学都难以跨越，期待这次跨栏成功。
️debug环节设置断点F9出现热键冲突。youtube看视频才知道了gutter是什么玩意…排水沟😩……还有breakpoint那个小红点点也太难找了吧！初步断点调试成功后面文本扩展没有继续深入。
️昨天就卡在用Jupyter notebook阅读这步，今天一步一步跟下来。原来昨天卡在了Advanced Settings没有添加命令成功，toc插件也安装成功自动生成了目录开心。

遗留问题：继续读书

day3
学号：1901050028
姓名：Hailey
学习内容：初步了解Python
学习用时：3h
收获总结： 
strings部分初步了解‘’和“”的区别，escape quotes的作用。
️numbers部分实现运算结合Tutorial明白了int和float区分的重要性。
️同样遇到打开VScode无从下手，分析原因是输入不够多，命令数据库无从调用。
意识到了未来Python官方Built-in Functions和Built-in Constants两节内容将是字典一样的存在。
️编代码部分参考了一个Youtube教程实现了小数加减乘除的基本运算。
发现一个括号一个符号都会导致运行失败，对于我这种粗心大意患者简直是机体强制改造。                                               ️运行较为顺利需要注意的是编程里的%和/是不一样的!!!不要异想天开%是计算除法的余数，比如5%2就得到1。
️最后测试运行环节发现Terminal计算完会闪退来不及看结果窗口就关闭了，搜索解决办法加入了一行命令input("Press <enter>") 。  想起曾经我有一个可以玩超级玛丽的函数计算器，向它致以由衷的敬意🔣

day4
学号：1901050028
姓名：Hailey
学习内容：掌握Python中条件判断（if elif else）和循环(for...while,break,continue)的用法
学习用时：6h
收获总结：
初步了解了
for循环：以集合为基础的循环
while循环：以条件为基础的循环
range的功能,
步长的用途
print的语法，
看到了print('some text', end='\t')往回翻才完全理解函数的默认设置，原来还可以反向操作...
遇到问题：
1.自动换行2.重复计算3.print字符串的语法
作业虽然完成了，还有很多需要巩固的。
今天真切体会到了笨拙和耐心。

day5
学号：1901050028


姓名：Hailey


学习内容：学习容器
学习用时：
2天
收获总结：
目前感觉最难的一次作业，资料多，任务重。
第一个小作业剔除包含ea的单词就卡住了，求助了助教明白了应该切分text成为列表，再for循环遍历。
后面学到了join把列表变为字符串
swapcase替换大小写
split分割字符串为列表
sorted默认排序
第二个小作业统计单词频次相对顺利
学到了用dict字典功能统计次数
sorted(dict.items(),key=lambda x:x[1])从小到大排列
如何清洗数据
第三个小作业
学到了reverse翻转，数组拼接字符串 s=s+str(a[i]) 参考了同学作业，
[]切片取出字符
[::-1]翻转字符串
转换为二进制，八进制，十六进制。
发现了stackoverflow.com救命稻草
有不理解的安慰自己是过早引用，继续笨拙前进！

day6
学号：1901050028
姓名：Hailey
学习内容：函数
学习用时：
5h
收获总结：
day5作业做的晕头转向。
踏实逐字看了看书,询问了助教day5代码中不明白的内容，很有帮助。做起作业比上次轻松很多，之前大多数时间是按任务跳着看书，一些地方理解的不透彻。
本次作业学会了定义函数，并封装。很有趣，学会了感觉方便自由很多。第一次任务中涉及到中文部分学到了如何提取中文汉字。看书时候着重看了dict部分，sorted(dict.items(),key=lambda x:x[1],reverse=True)之前这行只是运行，看书后对dict，key, value有了清晰的认识。统计次数排序也运用的更熟练些了。
Windows系统之前建立的readme.md文档是按照issue一个答案，建立文件在改成.md结尾，结果发现默认格式仍然是txt。回去查issue发现教练纠正了答案原来要在开启文件扩展名的情况下更改格式才可以，附地址，有同样问题同学可以参考https://github.com/selfteaching/selfteaching-python-camp/issues/1832

day7
学号：1901050028
姓名：Hailey
学习内容：掌握Python中模块的用法，理解代码的复用
学习用时：4hours
收获总结：
往后走其他同学的作业可复制性就很低了，所以前面自己的代码一定要搞清楚。基本代码越简但越好。
本次作业学习了在建立函数的基础上封装模块，再实现调用模块。
中文部分先做出来了，英文稍作修改也完成了运行。看别的同学作业里面引用正则表达式，count功能等，这样的话需要全部改掉自己代码，最后还是决定从自己代码入手更简单易懂。
遇到难点：
保留英文单词部分，询问了助教这段代码的意思。在t中遍历s是否是英文，如果是的话加入到list不是的话过滤掉。
for s in t:  # 只保留英文单词
        if s.isascii():
            list += s

day8
学号：1901050028
姓名：Hailey
学习内容：为函数添加参数类型检查
学习用时：2hours
收获总结：
今天作业内容仍然基于Day5，学到了判断函数中参数类型，提示错误及信息。在main中继续调用封装模块验证参数检查功能。
学习了if if type(text)!=str:
        raise ****语句
和用来捕获异常的try...except语句。
体验了互动版《自学是门手艺》，刷新阅读体验，感觉互动学习模式大有可为呀。

day9
学号：1901050028
姓名：Hailey
学习内容：初步了解Python自带的标准库，并学会如何查阅和使用
学习用时：5hours
收获总结：
耽搁好几天，恢复学习进度。
1、学习了Counter的使用，给函数添加Int类型变量count，实现限制输出元素个数。
2、正则表达式。
3、返回一个单词词频统计函数，样式为（word,count）
most_common([n])
>>> Counter('abracadabra').most_common(3)  # doctest: +SKIP
[('a', 5), ('r', 2), ('b', 2)]
比之前的写法简单很多。
4、读取json文件
遇到困难：用with open（‘workfile’）as f:方法没能调用成功，换成小楠教练指导的绝对路径调用成功。
继续前进！

day10
学号：1901050028
姓名：Hailey
学习内容：第三方库
学习用时：3hours
收获总结：
1、通过pip成功安装第三方库Jieba
2、基于day9作业修改代码,day9思路是遍历出中文汉字，再统计字典中汉字字频。day10的思路是引入jieba，筛选出中文字符串，拼接字符串后对字符串进行分词。引入字典，遍历统计分词后长度大于2的单词，按序排列前20词频。
3、遇到困难：按照之前代码dict={}，不能正常运行，改为dict=[]就可以运行了。一个小符号卡住1小时
感觉写代码很像拼乐高先找到大模块之后再慢慢调试不能着急。

day11
学号：1901050028
姓名：Hailey
学习内容：实战演练1
学习用时：3hours
收获总结：
1、通过pip成功安装第三方库yamail,requests,pyquery 
2、又复习一遍正则表达式。
3、第三方库太好玩了，想实现的功能感觉都有大神写好了。
4、提取内容比较顺利。getpass非常人性化，填写密码是不显示出来的。还一直以为自己代码有问题。
5、设置了邮箱的授权还是卡在了发送邮件上一直显示用户名密码有问题，参考Issue问了教练。试出来了一个能用的。密码不要写自己的密码，要填授权码。
现在看一些功能设置能想到一些背后的代码机制了，感觉又多一个维度看世界。还有太多不知道的想试试的，总之开始觉得很好玩啦~~

day12
学号：1901050028


姓名：Hailey


学习内容：实战演练1
学习用时：4hours
收获总结：
1、再次运用到了网络请求requests，文档解析pyquery 
2、安装引用了wxpy模块。
遇到困难：
1.引入语句根据readme：from wxpy import *没能正确调用换成了
from wxpy import Bot,Message,embed,SHARING可以实现了。花费了些时间，根据作业和issue调试成功。
2.sharing的内容不能是视频文件或者图片。
