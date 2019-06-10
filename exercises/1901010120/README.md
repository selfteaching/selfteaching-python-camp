
resolved一个#issue 3263问题,主要还是靠英文阅读能力
github是一个非常好的协同工具,可以线上线下协同,可以多项目协同,不知道还有什么好的功能可以挖掘挖掘,有点意思 

拓展:
git clone [url] //可以通说命令直接操作克隆
例如
$ git clone https://github.com/libgit2/libgit2
支持多协议:https以外,可以是git://,ssh,比如比如 user@server:path/to/repo.git
很方便 @_@//2019.5.30 23:08

day2记录
##
上次的拓展是GIT的,看到了git的全生命周期是4个,untracked,unmodified,modified,staged.
遗留的问题:
1.git和github的关系,是相互独立还是有一部分是相同的?
2.在VS code里除了commit,pull,还有push,pull和push的区别一直没明白

ref:
https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E8%AE%B0%E5%BD%95%E6%AF%8F%E6%AC%A1%E6%9B%B4%E6%96%B0%E5%88%B0%E4%BB%93%E5%BA%93

####
在阅读VScode环境配置的时候,发现了很多新的名词,简单的操作了一下,有选择解释器interpreter,debugging等,发现VS code也可以pull or push a commit,有点开发者的一个工具,不同在于个人习惯和功能缺失点,VScode和jupter notebook的面向对象和不同点还没有特别清楚,我估计也是随着实操的时间越久,理解会越深入.

另外有一个开发者的需求是关于虚拟环境的,一个项目可能会测试开发在不同环境中,其中包括python2.x或者3.x,所以需要针对一个项目或者不同项目来定义个人开发环境,所以
比如base conda envir,virtualenviroment in project folder,global envirments.conda envirment,其中有解释.
虚拟环境中可以针对不同的项目建立制定的解释器interpreter,尝试去google了一下,有这么几种办法来为多项目虚拟环境:
1)基于系统级别的切换,切换python2.x或者3.x. (我没有配置完成,没有做troubleshooting的工作) 
使用 Homebrew
2)基于本地通过Anaconda来创建虚拟的环境. (同样在source activate xx的时候有问题 stackflow了一下解决了) 特别强调一下anaconda的定义, 官方给的定义是:
Anaconda® is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 1,500+ open source packages.
打包和环境的管理器,客户对象是python/R的数据科学家.
3)还有一种就是升级版本,结合1和2的方法,把一个前端的环境打包放到azure上,可参考Flask Tutorial in VS code

上面说到package,什么是package.
1)官方给出的定义是:一个原始码的压缩包,其中包括模块和相关性信息matadata. update: canda的打包文件规则是xx.tar.bz2
2)channels里面可以包括整个package的全貌,类似树叶是package(包括树枝,树皮,颜色,位置等)而channels是一整棵书. 即jason文件
3)索引index可以用conda index <path to channel>
4)后面还包括真个build的过程和包里的文件说明,因为时间关系我大致略读了一下,没有仔细把玩,后续实践在把玩吧

A package is anything you install using your package manager
A "conda package" is a compressed tarball that contains
<b>the module to be installed
information on how to install the package</b>
You can use conda-build to build a conda package

Ref:
https://code.visualstudio.com/docs/python/environments
https://docs.anaconda.com/anaconda/
https://docs.anaconda.com/anaconda/packages/pkg-docs/
https://code.visualstudio.com/docs/python/tutorial-flask
https://conda.io/projects/conda-build/en/latest/concepts/index.html

