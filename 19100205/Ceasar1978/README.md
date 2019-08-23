# hello-world
3.21学习心得
今天是自学营的第一天。学习内容是GitHub的基本操作，参考资料就是Git官方文档（英文版）。有了前几天的预习，对于今天的学习内容并不太感到吃力，不过看完所有的参考资料再加上完成作业，也前后花了三个多小时。很庆幸自己这几年一直在坚持学习英语，今天才真正体会到笑来老师所说的“英语就是一双翅膀”，现在自己的英语水平能顺利阅读官方文档，这对学习效率是极大的提升。一切都刚刚开始，对未来的学习过程充满期待。
3.22学习心得
今天的学习内容主要有三项：
1、阅读Python环境变量的设置，这块因为涉及很多后期的应用，虽然英文能读懂，但是并不理解其中的很多含义，算是Forward Reference，等下再读一次，不理解的部分先放下。
2、通过谷歌搜索编写“Hello World”程序，编程倒没什么，一开始不知道怎么允许，最后还是谷歌搜索搞定F5键操作。也算是成功运行第一个自己编写的程序，蛮有成就感的。
3、用Jupyter Lab阅读《自学是门手艺》，这一步之前几天通过预习搞定了。

3.23学习心得
姓名：张凯山
学习时间：4小时
班级编号：19100205
今天的学习内容是了解python数值、字符串以及基本运算。参考文件讲的新概念太大，暂时不能全部消化。作业内容是编单步计算器的程序，一开始完全没有头绪。在网上找到一段程序，先阅读消化，之后又自己编了两次，运行成功。通过今天的作业，初步接触了函数和条件分支的基本操作。
感觉参考文档的难度还是很大，有必要先把《自学是门手艺》先尽快通读完毕，会有利于后期的学习。

3.24学习心得
姓名：张凯山
学习时间：4小时
班级编号：19100205
今天的学习内容是流程控制。作业要求用for和while分别打出九九乘法表，并且用while打出奇数行的九九乘法表。在阅读了《自学是门手艺》中关于流程控制的部分之后，重点分析了两种循环的特征，我在没有参考网上结果的情况下，独立完成了这三项作业，很有成就感。今天最大的收获就是通过实际编写代码体会到block这个概念的重要性，代码前面缩进几列涉及到一个block的界限，非常重要。也正是在多次调整语句前缩进距离之后，我今天的程序才运行得出正确的结果。

3.25学习心得
姓名：张凯山
学习时间：8小时
班级编号：19100205
今天的作业难度明显比前几天上了一个量级，第一题花了我几乎5个小时，当时真有深深的挫败感，后来是参考1期学员的作业再加谷歌搜索才理出了思路，然后一步步完成。第二题直接谷歌到答案，涉及到connection函数的应用，暂时还没搞明白原理。做第三题时又被数值list转换成字符串的函数问题卡住了很久，之前第一题里学到的join函数在这里不能直接应用，后来又是谷歌到了一个间接迂回的方法。目前是解决问题了，但是不知道还有没有更简便的方法（比如直接调用某个函数？）万维钢老师说刻意练习最好的环境是85%熟悉+15%意外，可这几天自学营的感觉是每天刚开始的时候熟悉的成分连15%都不到，越来越痛苦。但是克服困难完成作业之后的成就和喜悦也是越来越强烈。在训练营开始之前，我对自己能每天完成作业赢取学费奖励非常有信心，但到了今天，我的信心有些动摇了。已经挺过了五天，还剩九天，如果难度上升的斜率是如此陡峭，不知道自己能撑到第几天？不过无论最终结果如何，通过这几天的磨练我已经感受到了学习编程的乐趣，以后一定会坚持下去，耐心打磨这项有用的技能。

3.26学习心得
姓名：张凯山
学习时间：6小时
班级编号：19100205
今天的作业第一题基本就是昨天的延伸，所以比较容易就解出来了。但第二题看似和第一题一样，实际却有很大差别，想了很久，最后参考了一期学长徐悦的答案，他的解法很巧妙，几行代码就搞定了。虽然今天的作业并不都是靠自己独立思考完成的，但是能看懂学长的答案，通过这个过程也熟悉了很多基本概念，收获还是很大。
今日收获：
1、掌握了定义函数的流程。
2、深化了对数据结构和字典等基本概念的理解。
3、对于中文字符串，每个字是一个元素，可以用for i in text的方法来遍历，其中i是一个汉字。
4、可以用if u'\u4e00' <= i <= u'\u9fff'的条件来筛选汉字。
5、c =｛｝，c[i]=text.count(i),就是把i的计数作为字典c的第i个元素对中的第二个元素，第一个元素就是i。c.items()作用是列举字典c中的所有元素对。
6、countcn = sorted(countcn.items(), key=lambda item: item[1], reverse=True)的意义：sorted()函数用于对iterable进行排序，countcn.items()是排序对象，key=lambda item: item[1]，由方括号中的数字指定排序的是元素对中的第第一个元素，本题中就是汉字。item可以为任意字符，reverse=True表示由高到低。

3.27学习心得
姓名：张凯山
学习时间：5小时
班级编号：19100205
今天的学习任务是将昨天编写的两个函数整合成一个模块，并形成文件，再从另外一个文件中进行调用，相对而言比较简单。我的私思路是先统计中文词频，然后将中文字和标点都删掉，再统计英文词频，然后将两个结果（字典）合并，最后进行排序。，最终成功实现了这个结果。
今日心得：
1、原来用
for i in text：
    if i < n:
        del i
这种循环条件删除字符串中的元素是无效的，但运行并不会报错，暂时还不明白这个del是什么作用。后来是用replace命令实现的删除。
2、在合并两个字典时试了几项操作都无效，比如
dictMerged1=dict(dict1.items()+dict2.items())
dictMerged2=dict(dict1, **dict2)
好像是版本问题，这两个方法在3.x版都无效。最后是用连续两个update实现的。
d1={1:[1,11,111],3:[3,33,333]}
d2={3:[3,33,333],4:[4,44,444]}
d ={}
d.update(d1)
d.update(d2)
d.update(d1)前面不能加 d=，经测试，如果两个字典中有相同的索引，会被覆盖，无论冒号后的第二个元素是否相同。
3.调用文件和函数时一定要注意文件路径！

3.27学习心得
姓名：张凯山
学习时间：3小时
班级编号：19100205
今天学习任务是要求添加函数的参数类型检查并捕获异常，看了教程之后有了个大概的印象，但并没有全部了解。作业是参照徐悦学长完成的，用到了if not isinstance(text,str):这样的表达。教练说建议用try catch实现，但因为时间不够，没来得及研究透。后续再细化吧。
今日心得：
1、try前面不能缩进！（教程中的例子前面还有个while，所以要缩进）
2、 if not isinstance(text,str):条件判断text是否为字符串，是否为其他数据类型，还要搜索查询。


3.29学习心得
姓名：张凯山
学习时间：4小时
班级编号：19100205
今天学习的内容是标准库的引用和文件的读取。在之前第一次做词频统计的时候，就通过谷歌找到了connections.Counter函数，当时不太明白是怎么回事，今天知道这是标准库中的一个函数。文件读取之前也在《手艺》一书里读过，今天算是复习。过程中遇到了UTF-8编码的问题，总是报错，在教练的提醒下，看同学发的Issue解决问题。
今日心得：
1、with open('tang300.json','r',encoding='UTF-8') as f:
    text = f.read()
这其中f.read()输出的是一个字符串，encoding='UTF-8'可以避免编码报错问题。
2、今天编了判断闰年平年的函数，明白了if和“if then”是不一样的！
3、遇见程序报错，将错误代码复制到谷歌中搜索解决方法。

3.30学习心得
姓名：张凯山
学习时间：4小时
班级编号：19100205
今天的学习内容是安装和调用第三方库，安装方法通过谷歌很顺利就搞定了，调用方法也很简单。但是完成作业还是花了不少时间，主要是想通过.remove()函数实现列表元素的删除，但总是报错，最后想了其他的办法才完成。还有就是对汉字字符串的长度理解也出现了偏差。不过最后总算完成了作业，已经第10天了，大家继续加油！
今日心得：
1、安装pip：到网址https://pypi.org/project/pip/#downloads，找到Download files，下载pip-19.0.3.tar.gz，解压缩后，通过Juypyter Lab的terminal，用 cd 命令进入到刚才解压缩的文件中，输入python setup.py install命令。
2、通过pip安装第三方库：通过Juypyter Lab的terminal，进入pip所在目录，用python setup.py install命令。
3、一直想偏了，觉得汉字要经过编码，根据不同的编码方式，一个汉字的长度至少是2个字节，所以想2个汉字应该长度至少为4，实际上程序在统计汉字词语长度的时候，是将一个汉字长度计算为1的！
4、另外我最初的设想是用遍历判断每个词语的长度，如果小于2 就把该元素删除，用的是 list.remove(i)命令，但是报错'generator' object has no attribute 'remove'，暂时没搞明白原因，后来是用新建立一个空列表，把符合条件的元素用.append()命令添加进去解决的。

3.31学习心得
姓名：张凯山
学习时间：3小时
班级编号：19100205
今天的学习任务是使用之前的函数模块，再加上yagmail、requests和pyquery第三方库，提取网页内容并进行词频统计，同时将结果发送至指定邮箱。因为有两个库的用法在教材里已经直接给出了，所以今天作业的难度不大，比较顺利就完成了。不过仅仅是了解了这几个库的最基本的使用，要想深入了解，还需要后期更仔细地阅读相关说明文档。
今日心得：
1、输入的邮箱密码并非普通密码，而是一串经过编码的字母，要在邮箱网页获取。
2、用str_1 = str(dic)函数实现从字典到字符串的转换，不过这样得出的字符串，输出后看起来仍然是字典的样子，但用type()函数查看，显示的是字符串格式。

4.1学习心得
姓名：张凯山
学习时间：5小时
班级编号：19100205
今天的学习任务是通过wxpy库实现对微信消息中的网址采集，并进行词频分析后将结果返回给发送消息的好友。一开始自己通过摸索，能针对特定某个好友实现该功能。但后来看作业要求是对全体好友，最后通过参考徐悦学长的作业完成了。收获不小，但也发现现阶段自己的最大问题：对标准库和第三方库的各项功能还不够全面深入，虽然能完成作业，但有的地方还是知其然不知其所以然。后期学习需要继续夯实基本概念。
今日心得：
1、搜索单个好友应该用 my_friend = ensure_one(bot.search(u'好友昵称')) 这个函数
2、作业要求是对全体好友自动回复，我最初自己实现的功能只能针对特定好友。后来看了徐悦学长的方法，他使用了一个函数装饰器@bot.register(my_friend,SHARING),并定义了一个auto_reply(msg)函数。经分析，装饰器的作用是监听来自my_friend的消息，如果类型为SHARING（分享内容），即把消息内容赋值给msg变量。只是我不理解的是，函数返回的结果将直接自动回复给发送消息的好友（my_friend），这应该就是auto_reply这个函数的作用，但为什么这明明是个自己定义的函数，却能自带自动回复的功能？经过搜索，网上有介绍该库自动回复的方法，貌似auto_reply(msg)只要括号里的参数是msg，就自带将函数return的结果自动回复的功能，无论函数名称为什么。这应该是这个库的自带功能。
3、经与教练沟通，确认wxpy库有个自带功能，如果定义的函数return结果为str类型，将自动回复。

4.2学习心得
姓名：张凯山
学习时间：5小时
班级编号：19100205
今天作业是以图形化输出昨天的作业。一开始被counter函数的输出格式搞得有点糊涂，其实这个输出是二维list，而非字典。后来又卡在了如何将输出图片发送给好友上，提出issue后有高手指点，又参照了徐悦学长的作业，最终解决了。最后的问题是输出图片中的中文字都呈现方框，查了说是字体缺失。同班李浩天同学指出了方法,解决问题。
今日心得：
1、dic = collections.Counter(text_list1).most_common(100)这个函数的输出格式是二维列表（也就是说每一个元素也是一个包含两个元素的子列表），而非字典！如果要转换成字典，用dic=dict(list)函数。
2、根据wxpy库的特点，return只能将字符串自动发送到微信好友，今天作业要求是返回图片，所以要用到
    matplotlib.pyplot.savefig('words_frequency.png')
    msg.reply_image('words_frequency.png')
 先把结果保存为图片格式，再将图片发送。
 3、plt.rcParams['font.sans-serif'] = ['SimHei'] ，这一步是为了添加字体，否则汉字会显示为方框