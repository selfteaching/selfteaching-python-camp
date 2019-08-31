def stats_text_en(text):  #自定义函数，该函数用于统计参数text中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
    text1 = text.split()    #把字符串变成list格式
    text2 = []  #新建一个列表，用于存入处理过后的str          
    symbols = ",.-!*"   #整理出文本中需要剔除的符号
    for En in text1:    #在列表text1中遍历所有字符
        for symbol in symbols:  #如果包含symbols中需要剔除的字符，用replace语句替换掉
            En = En.replace(symbol, "")
        if len(En): #剔除了字符后如果单词En的长度不为0，那么就算正常单词，可以加入到新的列表中
            text2.append(En)
    #先把text中的符号剔除掉
    text3 = " ".join(text2)
    text3 = text3.lower()
    #把所有的单词变成小写格式
    text3 = text3.split()  
    #把text变成list格式
    d = {}   
    #采用空字典形式保存结果
    for i in text3:    
        a = text3.count(i)
        d[i] = a  #统计text2中i的频次a，并将结果导入字典
    d1 = sorted(d.items(), key = lambda item : item[1], reverse = True)
    #将字典里的元素按照value的降序排列
    print(d1)
    return

text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
stats_text_en(text)

def stats_text_cn(text):
    text1 = []  #设置一个空列表用来存储中文字符
    for cn in text:     
        if '\u4e00' <= cn <= '\u9fff':  #判断text中的每个字符是否属于中文字符，是的话就加入到列表text1中，中文标点符号都去掉
            text1.append(cn)
    d = {}  #新建一个空字典保存统计结果
    for zh in text1:
        d[zh] = text1.count(zh)  #将统计text1中的字频a导入到字典d中
    d1 = sorted(d.items(), key = lambda item : item[1], reverse = True) #以字典中的频次value进行从高到低排序
    print(d1)
    return

text = '''
1. 将本地仓库关于本次作业的变更更提交为⼀一个 commit
2. 通过 Github 桌⾯面客户端将本地电脑的变更更推送到⾃自⼰己账户下的作业仓库
3. 回到 Github ⾃自⼰己账户下的作业仓库⻚页⾯面，向远程公⽤用作业仓库的 master 分⽀支发起 Pull
Request，在提交的 Pull Request 的标题（title）中填写⾃自⼰己所在的钉钉群名，如示例例：
【032901】⾃自学训练营 DAY1 ，并在评论（comment）中 @⾃自⼰己的助教（请向助教索要他
的 Github ⽤用户名）提醒他检查作业
'''
stats_text_cn(text)
