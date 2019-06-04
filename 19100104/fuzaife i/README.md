学习心得

自学训练营第一天课程。

任务一之前预习就已经完成，用户名 fuzaifei已经发送给辅导员。

任务二 ：创建⼀个⾃⼰的代码仓库，学会使⽤分⽀（Branch）和Pull Request
a. 阅读参考资料1
b. 创建⼀个名为 helloworld 的仓库，并在仓库内创建两个分⽀ master 和 develop
c. 在develop分⽀中创建⼀个名为 develop.txt 的⽂件，提交⼀个commit
d. 从 develop 提交⼀个 Pull Request 到 master 分⽀，并将其合并（merge）
e. 在master分⽀中再创建⼀个名为 master.txt 的⽂件，提交⼀个commit
f. 从 master 提交⼀个 pull request 到 develop 分⽀，并将其合并

任务二备注：  
熟练创建仓库，第一次成功创建分支，直接在仓库主页面的branch的选项， 单机就会出现下拉菜单，填好分支名字就可以直接创建新的分支。master是默认的主分支，不用重新创建。               疑问在之前预习的时候为什么没有学会？
如果要创建一个文档，需要先选择好分支，否则就是默认的主分支（不过创建新文档的提交的时候也可以选择提交到默认分支或者是否创建新的分支）。

在F小任务提交的时候遇到了难题，没有一次就成功提交request。
如下：在选择new pull request之后打开新的页面，在master分支下没有看到我之前创建的master.TXT文档？  点击验证后，也没有明显的改变，但是文件还是在master之下，从develop提交到master合并后，文件是转移到master了。
我重新在master分支之下创建了新的文档，这一次可以pull到develop分支中了，多次创建新文档尝试。
成功完成任务二。

任务三：在⾃⼰的本地电脑，安装 Git 桌⾯可视化⼯具 SourceTree，管理远程仓库
a. 阅读参考资料2，3
b. 通过下载地址 https://www.sourcetreeapp.com/ 安装SourceTree软件
c. 在⾃⼰创建的 helloworld 仓库中找到 clone with https 的地址
d. 通过 SourceTree 将 helloworld 仓库 clone 到本地仓库
e. 在本地仓库中创建⼀个名为 local.txt 的⽂件
f. 将本地仓库新增的⽂件提交为⼀个 commit
g. 通过 sourcetree 将本地电脑的变更推送到⾃⼰账户下的 helloworld 仓库
PS:
a. 因为sourcetree⽐github官⽅版本好⽤太多，所以要求⼤家使⽤sourcetree

备注：之前在预习的时候根据下载了好几款软件，都没有弄懂，已经卸载，安装训练营提供的。（突然死机了，还好重启，文档还在，应该是提供云缓存）
需要翻墙网络不太好，sourcetree 注册安装花费了30分钟左右。
e任务没有找到在本地仓库如何创建一个新文件。   处理方法：在本地仓库的文件夹直接创建一个txt新文档就ok。
新问题：无法提交。   处理：已经解决。需要把未暂存文件，修改为暂存所有，就可以提交了。

任务四：在其他项⽬中贡献⾃⼰的代码
a. 阅读参考资料4
b. 将公⽤的作业仓库（https://github.com/selfteaching/selfteaching-pythoncamp） fork 到⾃⼰账户下
c. 向辅导员或教练确认⾃⼰的班级⽬录，如 19100101
d. 将⾃⼰账户下的作业仓库 clone 到本地电脑
e. 在班级⽬录下，创建⼀个⽤⾃⼰的 github ⽤户名命名的⽂件夹（这个⽂件夹是将来写
作业的地⽅），并在⾃⼰⽤户名的⽂件夹下创建⼀个名为 README.md 的⽂件（这个
README.md⽂件可⽤来记录分享⾃⼰的学习⼼得）
f. 在⾃⼰⽤户名的⽂件夹下创建⼀个名为 d1_exercise_helloworld.txt 的⽂件，在⽂件中
写⼊任意内容
g. 将本地仓库新增的⽂件提交为⼀个 commit
h. 通过 sourcetree 将本地电脑的变更推送到⾃⼰账户下的作业仓库
i. 回到 github⻚⾯，在⾃⼰账户下的作业仓库⻚⾯向远程公⽤作业仓库的 master 分⽀
发起Pull Request, 在提交的 Pull Request 中 @⾃⼰的教练 提醒他检查作业


备注：在班级目录104下创建文件夹失败，只有创建的地方，疑问：文件夹=新分支吗？不是的，需要在本地创建一个文件夹。
提交失败  教练告诉我删除本地克隆，然后从新克隆，提交文档成功

第一天任务完成，用时在3小时作业，在教练的帮助下相对而言比较简单。昨天自己在按照考高资料下载一些软件安装的时候基本不知道头绪。有些地方，只要一点指示就过关了，然而往往就是这些关键点不知道。
加油，下午在复习一下

10月19日

任务一二完成

https://www.anaconda.com/distribution/在下载地址下载完成，并且安装好相关插件。

跟着http://docs.anaconda.com/anaconda/user-guide/getting-started/#write-a-python-program-using-anaconda-prompt-or-terminal   跟着Anaconda入门学习;

跟着https://conda.io/projects/conda/en/latest/user-guide/getting-started.html    学习conda入门指南。可以在conda通过代码python配置python。通过代码Spyder打开spyder ;通过代码jupyter-notebook打开notebook。通过代码  conda update conda  检查是否是最新版本，并且用y确定更新，系统建议用最新版本。

通过代码 conda create --name snowflakes biopython  创建一个 snowflakes 的新环境。 也可以自己随便换名字。我创建了一个 newfuzaifei 。当确认之后，需要出现很多代码，虽然不知道什么意思，估计就是开辟新环境。当用键入代码 conda activate newfuzaifei之后，在新的代码行的base换成了newfuzaifei。不过通过键入代码 conda activate 更改回默认环境没有成功，提示不是内部命令。

Jupyter笔记本应用程序是一个服务器-客户端应用程序，允许编辑和运行笔记本电脑的文档 通过网络浏览器。所述Jupyter笔记本应用程序可以在本地桌面无需网络连接通过因特网（如本文档中所描述的），或者可以安装在远程服务器上，并且访问上执行。


任务三：编写程序。
用jupyterhe和studio code分别写了一个d2_exercise_hello_python.py的程序
在登录sourcetree的时候，电脑太卡。成功打开，然后上传py程序，然后推送给教练。


整个运营环境还是很关键的，如果没有指导，很不让容易成功安装。不过通过官方的文档还是可以比较容易安装。

用时1小时左右。


10月20日  完成时间2小时。
第三天学习

参考任务一的资料，了解python的用法。
在conda界面把参考资料中的所有代码重新到了一次。学到了一些用法：

数字，运算符，字符串的单词之前都用一个空白符。虽然我尝试数字做运算是不用空白符，不过不是太好看，不过尽量让自己养成习惯空白符的习惯。
\\是整数结果，忽略小数点，相当于int()'；%是余数；**是乘方；反斜杠\是转义的用法，在原始字符串之前加了r就不会转义（\n表达是后面内容是在新的一行，在最前面加入r之后就不会转义。）
'''....'''或者"""...."""是跨行输入。
如果数字和字符串之前出现*是表示字符串被连续打印3次，+是表示连接的意思。
赋值变量好像直接可以跨行。相邻两个引号引起来的字符会被自动连接在一起。
给一个变量赋值一个字符串，可以在下一次这个变量后加【数字】这样是截图索引，对应数字的字符串的字母是什么；如果是负数，则从右边开始；负数索引是从-1开始，正数是从0开始。
内建函数len()返回一个字符串的长度。
列表的内容是可以改变的。immutablede 的字符串是不可以改变。

以上用时1小时

append加元素，pop是尾部删除元素。del删除任何一个元素；in测试列表是否包含；len()取列表长度。
if。。elif...else 判断， 如果怎么就怎么，不然怎么就怎么，否则怎么就怎么
for循坏列表所有
range(number)返回数字列表从0开始。我打印了一个while i in range(4),print(i),竟然出现无限打印3.   while循环知道条件不满足。

40分钟看完参考资料2 。

最后的一个程序。

![微信截图_20190320114448](D:\Desktop\微信截图_20190320114448.png)

