# 课程总结

# Github
除编译器之外的重要协作软件Github，其功能类似于编程版本的Google Doc，可以允许多人同时编程。
对每段更改保有历史记录，可回溯任意更改，避免代码被覆盖，且可回溯任意版本。
Github建立在分支架构之上，主分支负责程序主体，dev分支则可供个人修改使用。个人修改的程序可通过pull request请求并入主分支。此功能保证多人同时协作的同时，亦可以避免程序被个人错误更改。
通过folk加入其他repository，通过clone下载到本地，通过commit讲更改提交到主分支，通过pull request将修改提交。

# Python 编译器
Anaconda-Navigator 综合了数个python编译器。
Visual Studio Code适合快速编译python shell内容，界面视觉效果较好。Spyder适合做短代码测试，界面一般。
Visual Studio Cose 和 Spyder 保存的代码可以自动同步，方便转换。
在python shell中需要print将数值显示，否则默认隐藏。

# Hello Word
约定俗称的语言入门所编写的第一个程序。
Print作为python输出，在python shell内不print的内容默认隐藏。
print时以'/t'控制同行空格打印。
print时以''换新的一行。

# 结构类型
有字典（dictionary），元组(tuple)，列表(list)等储存单位。
元组和列表是以位置储存元素，位置0对应第一元素，位置1对应第二元素，构成元素和位置一一对应的关系。
字典是以key和item进行一一对应。
元组内部数据无法更改。
字典用于统计数字较为方便。

# 循环
for loop 和 while loop是最常用的两种循环模式。
for loop不仅可以进行数字循环，也可以进行列表中元素的循环。
while loop可以通过 while True 不断循环直到达成条件break。
break会跳出最内层的循环。
当过多循环减慢速度时，可采用numpy替代。

# try...except
阻止程序进入error，可保证代码继续运行。
可暂时忽略无效代码。
配合try...except然后print，可进行debuging。

# Debug
bug可以双轴分为四象限：横轴为显性，隐性；纵轴为持续性，间歇性。
隐性bug比显性bug危险，间歇性bug比持续性危险。
显性bug程序会直接报错，易于发现；隐性bug程序不会报错，但输出结果与预期不符，更难发现。
持续性bug每次运行都会出现，间歇性只会在特殊情况下出现。
千年虫既为典型隐性间歇性bug。
Debug过程，需要讲代码分为不同模块，检测不同模块结果，发现模块结果错误既修改之。
修改单一模块后，仍需整体运行以保证输出正确。

# 排序
计算机编程的重要组成部分。
不同的排序方式会产生巨大的速度差别。

# 模块
将已经编写好的代码作为模块保存，可以在其他程序中进行调用。
调用所需时间较长。
可使得程序简洁明了。

# 画图
画图逻辑与matlab相似。
需要导入matplotlib包函数。
处理速度相对较慢。
matplotlib包本身不支持中文，故需要通过一下代码导入中文：
    lt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']

# yagmail
可进行收发邮件，配合try..except使用，可保证在程序出错时迅速收到提醒。
邮件发送前邮箱需要授权Pop/SMTP。
授权后以授权码代替密码。
getpass默认隐藏密码，输入不可见。
yagmail.SMTP()中host需要输入，否则出现超时错误。

# getpass
可用于获取密码，其特点为密码会呈现不可见状态，以保护密码安全。

# wxpy
微信外链程序，可编写自动回复脚本。
基于webweixin进行，有可能被微信web封号。

# jieba
中文分词包，其共嫩建立在内含的词典之上。
可通过jieba进行词频统计。
jieba输出为不可见的list形式。

# 自学相关
凡是知道方向，大部分问题都可通过搜索引擎解决。
寻找方向是自学的关键。
自定一个Project，以解决问题的形式进行学习，倒逼学习相关知识。
自学可能产生回音室效应，产生自循环，也就是倾向于用已知知识解决新问题，因此需要时时与他人对比。
部分问题已经有人做出更好解答，不可迷恋自身能力。
相对于系统化学习，可能漏过部分基础，使得无知于某些高效解决方案。