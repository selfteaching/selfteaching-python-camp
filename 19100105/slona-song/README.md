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
