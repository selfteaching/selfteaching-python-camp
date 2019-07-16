学习心得 Day5

1. 学习内容
各种数据类型、dict
2. 学习用时
9小时18分
3. 收获总结

Task 1-剔除单词

如果要删掉单词的话，应该用lstrip语法，但是死活看不懂它是怎么运作的，教程的中文版看起来想第二外语，还不如直接看英文版。

看不懂的话，只能用笨方法了，修改各个部分的内容，然后多次尝试，看看会输出什么结果。跑代码的过程还是很愉快的，虽然大多数时候都提示我错误，好歹也算是即时反馈。单纯看文档是会崩溃的，越看越不懂，持续打击哦。

果然，代码一跑起来，我就明白了。我分别尝试了：
>>> 'www.example.com'.lstrip('cmowz.')
'example.com'
>>> 'www.example.com'.lstrip('e')
'www.example.com'
>>> 'www.example.com'.lstrip('w')
'.example.com'
>>> 'www.example.com'.lstrip('wwww')
'.example.com'
>>> 'www.example.com'.lstrip('.com')
'www.example.com'
>>> 'www.example.com'.lstrip('w.e')
'xample.com'
我终于明白文档里说的leading character的含义了。这东西用文字来解释是真繁琐，用扑克牌来解释就简单不过了。

'www.example.com'.lstrip('cmowz.')代表我手里扣着十五张扑克牌，从上到下分别是w w w .  E x a m p l e .  C o m，桌面上亮着六张牌，分别是c m o w z . 。现在从我手里亮出最上边的那张牌，如果跟桌面上的牌能配成一对，就扔掉。桌面上牌不动，再从我手里亮出第二张，重复上一个动作，直到无法配对。此时我手里剩下的牌，就是代码的输出结果。

但这个不适用于任务，完全不相干。同理str.rstrip这个也不适用，是从底下往上翻扑克牌的。

str.strip这个就难了，不仅上下同时翻，还玩起了顺子。手里连续的牌，如果能和桌上牌拼出的顺子相同，就可以消掉，条件是，必需从头顺或从尾顺。但这也不适用。

如果不能直接达到目的，应该是要分两步，先找出含有ea的单词，然后删除这些单词。
find，index等语法都只能找到第一个结果，不知道是不是要用到find all，要import re什么的。实在没有思路了，就去同学那里copy一下。
for i in text.split():
    if i.find('ea') < 0:
    word.append(i)

但是竟然用了split，这又是为什么呢？原来电脑不认识单词，不知道字母之间是怎么划分的，所以需要告诉它，要以空格为分隔，划分出一个个单词。text.split()就表示已经用空格分隔好的text。i是文本中的一个个单词，如果在i里边找到了ea，就把它删掉。这个<0又是干什么的？关键问题是，这个代码跑不动啊….换一个人的吧。

text3=text2.split() 
text4=[]  
for word in text3:
    if 'ea' not in word:
        text4.append(word)
    text4.append(word)
text5=' '.join(text4)

这个童鞋的代码很清晰，还有备注。但是，他们都不print吗？无论代码对错，总是要输出的吧？

想copy也不容易啊，这个同学的代码也有问题啊。又换了一个同学的。

c=b.split()
    d='ea'
    e=[]
    for i in c:
    if i.find(d)<0:
    e.append(i)
    print(e)

if i.find(d)<0:的意思是，如果在i里边找d没找到，就把i加到e里边。
原来如此！代码不是要挑出包含ea的所有单词，而是要挑出所有不含ea的单词，把他们放在一起。其实挑出来应该好挑，用if i.find(d)>=0应该就可以，但是想把它们删掉就不容易了，扑克牌只能从顶部或底部抽。

但是这个代码跑出的结果，所有单词都加上了引号，这效果很别扭。用join加上空格就是正常句子的样式了。不过一句话一行是实现不了了。

join语法是这样的：
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
输出结果分别是
r-u-n-o-o-b
runoob

Task 1-转换大小写

转换大小写字母用swapcase就可以，但是Instance of 'list' has no 'swapcase' memberpylint(no-member)，上一个任务的结果text3用不了这个语法，用text原文就没问题，我猜可能是text3的属性变了。

Task 1-单词排序

本来以为排序很麻烦，结果一个print(sorted(text3,reverse=False))就搞定了？

Task 2-统计单词出现次数

dict的材料看了很多，就是没懂怎么往dict里边加东西，教程里都是把每个元素写出来，然后往里加，文本那么长，这么加怎么行？于是参考了童鞋们的作业，不得不感慨一下，每个人的代码都不一样，很是神奇。dict = {}, if i not in dict, dict[i]=1,就把所有的i加到dict里了。if i in dict, dict[i] = dict[i]+1就是数数了。

Task 3-数组操作

越往后越简单了，翻转就用list[::-1]，取片段就用list[2:8]这在最开始就学过了。转换进制也不难，分别是bin(list4)，oct(list4)，hex(list4)。

4. 遇到的难点与问题
dict还不是很理解。
把一个元素里的东西挑出一些组成新的集合，再用空格替换掉'',数据类型为什么就变了，无法理解。

——————————————————————————————————————————————————————————————————

学习心得 Day4
1. 学习内容
用for函数和while函数编写九九乘法表

2. 学习用时
4小时+

3. 收获总结

虽说遇到问题要先自己想办法解决，但是配置文件的问题还是不要随便改。我在网上搜了N多种python2升级为python3的方法，好用的不好用的都操作了，结果把vscode改得乱七八糟。教练远程帮我检查问题，前后得有三个小时，复原了N多处修改，还是抵不过vscode任性。

教练灰常有条理，又有耐心。我不把python学好都对不起教练QAQ。

远程处理配置问题时，我学到了一些小技巧：

Vim xx 文件
hjkl是上下左右键 ，退出按 ：q  保存并退出按：wq
在terminal 里，ctrl+a是跳转到最左边
输入一部分文件名之后，按tab会自动补全，按两次tab会出现所有符合的文件名。
sudo rm -f 是强制删除，但是我的user文件任性，就是不让删，写了保护，要到安全模式关闭保护才能删。
两个命令之间用&&连接 可以同时运行，用&连接的话 会被挂起
在网上搜索资料的时候经常能看到print后边有的有括号，有的没有括号。前者是python3，表示的是一个函数，后者是python2，表示什么我忘记了，但是不重要，记得都加括号就好。q

至于九九乘法表，自己想破脑袋也想不出这个逻辑，在网上搜索之后，对for j in range(1, i+1)稍微理解了一点。对于while语句的理解，目前只有i += 1要在print之后，还得多看、多用过一些才能更好地掌握。

4. 遇到的难点与问题

检测过程中发现了一些问题。我多次安装过anaconda，但是位置不一样，一次是安装在根目录，一次安装在用户目录，所以vim文件里被写了两次。

系统自带的terminal是没有问题的，在vscode里调用python3运行文件，可以成功运行，但是之后又被某个命令或设置覆盖成了python2。问题根源在哪始终没有找到，暂且的解决方案是，打开vscode之后，运行conda deactivate && source ~/.bash_profile。就是把conda关掉，强制使用系统的python。
————————————————————————————————————————————————————————————————————————

学习心得 Day3
1. 学习内容
各种函数
制作计算器
2. 学习用时
10小时+
3. 收获总结
任何代码都要自己亲自输入，然后尝试各种修改，测试是否还能跑起来，以此来理解什么样的代码才是有效的。

如果想在终端里使用计算器，那么需要先输入Python，进入Python的语言才能使用。

python里的加减乘除和一般的计算器符号一样。特别的符号有：
17%5=余数
**乘方
顺路还学习了2的7次方的英文说法，2 to the power of 7。
_代表上一个计算结果。
负数的符号”-”的优先级高于乘法和除法，但是低于乘方，所以计算负数的乘方是要加括号，比如：（-5）**3。

输入True or False的时候首字母必需大写。

给word赋予一个string，word[0]表示第一个字母，word[-1]表示倒数第一个字母，word[2:5]表示第三个到第五个字母，[]含头不含尾。这样是为了确保word[:2]+word[2:]=word.第一个字母用0排序是为了使word[:2]表示前两个字母。

赋值了string后，不能修改单个字母，但是用列表[]赋值的变量，里边每一个部分都可以增加、删除、修改，无论是数字还是string。

列表可以套列表，X[0][1]表示列表X中，第一个列表里边的第二个字母。

如果需要输入多行文本，就在段首使用三个引号”””，这样的话，按了回车后可以继续输入，而不是立刻执行命令。两个引号都不行，必需得三个。
for i in range(4):
    print(i)
对于这种多行的代码，一定要缩进，不然会出错。

越往后的代码越难理解，只好在实践中学习了。

可用在面试时的英文回答：It is now one of the most popular languages in existence. I fell in love with Python for its syntactic clarity.

助教远程帮我解决了环境的问题，环境配置什么的还是不要随便改的好。
source activate base 用这个命令来激活环境，base可以替换成对应的环境，比如训练营专用的pycamp

4. 遇到的难点与问题
已解决
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...

不懂这个地方怎么敲，阅读中文指南后各种尝试，终于搞清楚了。
while a<10: 打完之后，回车，按Tab，输入第二行，回车，再按Tab。所有内容输入完毕后，回车两次。

参考资料1里讲Division (/) always returns a float. 但我的terminal不给float，强制int。
在教程里看到：
# If your Python 3 code also needs to run on Python 2.5 and below, you can also
# still use the old style of formatting:
"%s can be %s the %s way" % ("Strings", "interpolated", "old") 
才想到某种可能性。把这行代码敲进去，真的可以运行，然后查看了下版本，才知道是2.7。要不是教程里有这句话，我还在跟自己较劲呢…
回顾了下前两天的课程，没有下载python的这个步骤，我也不知道电脑里的python2.7是哪里来的，也许是电脑自带的。

Brew install python3之后，terminal里python版本变成了3.7，vscode里，左下角的环境已也变成了python3.7唯独vscode里打开的终端，仍然显示为python2.7。

尝试用网上的搜索结果一通乱改之后，interpreter的选项不见了。

干脆把vscode和anaconda都删除重新安装。

重装anaconda的时候系统提示：“安装失败，该软件已经安装。”肯定是删除不彻底。Mac的系统这一点就比Windows麻烦很多，在launchpad里搜不到anaconda，专用的系统清理软件也找不到。最后只能用terminal输入命令，安装anaconda-clean才彻底删除。其中删除配置变量的时候，要使用vim，这个vim也是很神奇，网上搜到的指令很多都运行部了，连退出都得强制关闭，只好放弃。

几经波折终于重装好了vscode，在配置环境的时候突然想到，会不会是我查询版本的时候输错了指令。python —version的结果还是2.7，但python3 —version的结果就是3.7了。电脑的terminal里python —version的结果直接就是3.7。不知是显示的差异，还是默认版本的差异，可能误导我做了一天的无用功。

因为这个差异，在vscode里启动python的时候要输入python3，而不能是python。

想要运行python文件时，又说Linter pylint is not installed，点击弹出框里的install没有用，只能用pip install pylint命令下载。

下载时提示路径不对，还是vscode的设置不对。之前在百度用中文搜索，没找到对症的结果。这次换成bing，用英文搜索，很容易就在Stack Overflow里找到了和我情况一模一样的问题。确实是要修改路径，不仅要修改用户的，还要修改工作区的设置。

打开.bash_profile，在最后一行加上alias python=‘python3’。

至此，表面上的问题都解决了，我终于可以做计算器了。

参考网上的计算器代码进行编写，逐渐找到思路后，发现有些问题。代码的本意是想在选择加减乘除的时候，如果choice不等于1234，就提示输入有误。结果呢，但凡计算结果不等于1234，就会出现错误提示。我想用while，for函数来实现，但是试来试去逻辑都不对。最后参考了一个python2时代的代码，把choice的属性都改成了int，然后在最开始的时候限定1<=choice<=4，就能达到目的了。



未解决

没看懂bool函数是什么意思。

修改了python的版本和路径，但pip install的时候还提示版本将在2020年失效，这个等遇到的时候再想办法吧。

float的小数位有时候很迷，无法理解。
>>> 99.9/100
0.9990000000000001
————————————————————————————————————————————————————————————————————————

学习心得 Day2

1. 学习内容
安装和设置Python的运行环境，自己搜索学习编写hello world。
2. 学习用时
共用时2小时7分钟
3. 收获总结
大致了解了终端、vscode、GitHub之间的操作关系
我发现，在vscode里边点击Terminal，会在file下方出现terminal的界面，和从mac里打开的terminal功能是一样的，还不用来回切换界面，方便了很多。
4. 遇到的难点与问题
已解决

没有搞清楚怎样在vscode里边切换路径，但是换了一种方法实现了。
先关闭vscode，然后在终端里cd到指定目录，然后用code .命令再打开vscode。

如果此时终端从另一个路径code .会怎样？试了一下，会打开一个新的vscode窗口。

旅游一个星期回来，连commit都忘了，重新学习了day1的内容才想起来。

在GitHub desktop里，push origin的界面必需在所有changes都commit了之后才会出现吗？
我的学习心得还没写完，暂时不想commit，就没有单独push origin部分changes的办法吗？
测试了一下，是可以的，在顶部的界面框里点depository，再点击push，就可以只push已经commit的部分。

未解决

今天的任务已经完成了，但是还没搞清楚anaconda是做什么用的？只是用来下载vscode等软件？编程的时候可不可以关掉？试了一下，好像没有任何影响。vscode软件还在，终端也可以使用，anaconda的环境也在，似乎编程的时候不需要单独打开它。下次试试。

在vscode里写学习心得，编辑文档非常不方便，不知道markdown的格式在这里可不可以用。
————————————————————————————————————————————————————————————————————

学习心得 Day1

1. 学习内容
今天学习的是GitHub的使用，主要是新建repository，pull，push，clone，fork等基础的操作。
2. 学习⽤时
共用时1小时58分
3. 收获总结
之前也用过GitHub，但是完全不理解，只是按照教材照着copy。这回从GitHub的官方指导手册开始阅读，对整个逻辑框架有了一定得理解。
把别人的内容复制到自己的账户里叫fork。
把自己账号里的内容复制到电脑里叫clone。
在自己电脑里修改内容后要commit。
要把修改的内容更新到自己的账号里叫push origin。
想把自己账号里的东西合并到原作者的repository里要pull request。
4. 遇到的难点与问题(是否解决)
原来有一个GitHub账号，ID是evlyn5，但是上边有一些改得稀烂的repository，所以想干脆重新注册一个号。
我把旧账号的ID改成了evlyn555，把evlyn5的ID让给新账号。但是新账号用新浪邮箱注册，一直收不到验证邮件，
我只好用回旧账号，ID也只好再换回去。
然后问题就出现了。
GitHub和desktop登录的都是evlyn5的账号，但是exercise的最新记录显示的却是evlyn555刚刚commit过。
理论上讲，GitHub和desktop必需登录相同的账号才能clone和commit。但是为什么出现我这种情况呢？
这个问题描述起来很麻烦，我找了很久也没找出症结所在，索性放弃了。
毕竟这个问题不重要，以后不登录evlyn555这个账号应该就没问题了吧。
但是，如果在实际工作中出现这个问题，可能会给teamwork带来一些困扰吧，而且接收notification也会受到影响。
