import collections
#英文词频统计，重心是次数。（刚开始的时候还分不清楚）
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

def stats_text_en(y):
    '''
    if not isinstance(text,str): # 添加参数类型检查
        raise ValueError('输入的不是文本格式，请重新输入：')

    
    #n = []
    #for line in n:
        #line = line.strip()           #strip()这个函数去除一个字符串首尾的所有空白
                                       # ，包括空格、TAB、换行符等等。搞笑的是昨天
                                       #居然还在括号内添加了空位符                                   
        #if len(line) == 0:
            #continue
            #for x in range(0,len(line)):
                #if line[x] in [',','.','\n','*','!','--']:
                    #continue
                #if not(line[x] in n):
                    #n.append(line[x])
    #以上内容先放这里，后期，等全部内容学完了，再来回顾。
    n = y.replace(',','').replace('.','').replace('\n','').replace('*','')\
        .replace('!','').replace('--','')
   #以上语句如果说字符串是不可变的，那为什么我可以把,.*!这些字符给替换掉呢？
    #所说的不可变是指什么方面不可变呢？
    n1 = collections.Counter(n.split(' '))
    #return n1
    #return在自定义函数内必须返回一个值（个人理解）
    #有表达式就得跟在return后边，否则返回的只是一个None值
    #unexpected indent(意外缩进)要着重关注
    n2 = sorted(n1.items(),key=lambda x:x[1],reverse=True)
    #如果需要指定按哪个值进行排序的话就要对sorted函数里面的值做更改
    #这还是猜的，后续要搞明白这个原理
    return n2   
#print(stats_text_en(text))
'''
    import re                      #9day
    import collections
    words = re.findall(r'\w+',open(y).read().lower())    #打开文件的格式r''.open('').read()lower.
                                                   #这个例子只是直接省略了后面的lower
                                                   #再次使用正则表达式，通过google知道，
                                                   #原来正则表达式并不是python的一部分。
                                                   #正则表达式是用于处理字符串的强大工具
                                                   #现在比较深刻的理解了正则表达式的强大
    count = int(input("您想统计前多少个词频最高词："))
    list1 = collections.Counter(words).most_common(count)
    return list1












#中文字词频统计
#character = 
'''
  记录问题是自学的根本。今天，钉钉群里看到有位同学  
可能是因为没有跟上训练营作业的进度，于是心生焦虑，
出现了一点抱怨的情绪。其实对于新手的我们来说，我
非常能够理解他的心情。因为成年人要自学一门手艺，
本身就要克服很多客观存在的现实条件。如，工作和家
庭。再加上，编程这门技术，用的是英文，很多时候如
果不求其解，囫囵吞枣的把作业做完，确实可以。但是
我相信，既然大家，下定决心报名参加训练营，肯定是
想在整过训练营中的每一天都有所收获。然而，因为没
有任何基础，而且要在短时间内要完成布置的作业，对
于英语和编程小白来说，肯定是一种挑战。这个过程，
一不小心浪费了时间，就可能被训练营的进度甩到身后
。 让人对进度无力回天，无奈叹息。但是，话又说回来
，既然你想收获一些什么，你肯定要去经历和经受一些
曾经自己不曾经历和经受过的东西。只有这样你才能有
所收获。真的不是说你交了钱，那知识和技能就会自动
形成于你的大脑之中。不管多牛的人创造出来多好的知
识，那些知识也只能是属于那个牛人。如果，你想把那
些理论的东西变成你自己的能力，你就必须要全身心的
投入时间和精力去吸收、理解、运用那些知识。运用、
运用、反复运用，只有这样，这门手艺才有可能娴熟于
你。不过做任何事情，都是有方法可循的，一个人埋头
苦干，不仅累，到最后可能颗粒无收。既然，创建这样
的一个训练营，那么肯定是为了你在学习上遇到困难的
时候，有人和你一起交流探讨。三个臭皮匠胜过一个诸
葛亮。永远要相信大众的智慧。同时，为了珍惜自己和
别人的注意力，你应该把遇到的问题用专门的文档记录
下来。等到积累一定问题时，拿出来统一讨论。即使很
多问题不用拿出来讨论，自己把它记录下来，也方便自
己回顾复习。我赞同训练营主任的提议，就是在自学的
过程中把遇到的任何问题都好好记录下来。我想这也是
必然正确的自学方式。加油，自学就是要不断针扎，训
练营给我们的不是这短短的14天时光，而是终生的自学
能力，每天尽可能的把作业做完。绝对不能放弃，坚持
一定会看到不一样的风景。
'''

def stats_text_cn(y):
    import re                                     #9day
    import collections
    import jieba
    words = ''.join(re.findall(r'[\u4e00-\u9fa5]',y))    #打开文件的格式(r''.open('').read()lower.这个不适合用在这里)
                                                   #这个例子只是直接省略了后面的lower
                                                   #再次使用正则表达式，通过google知道，
                                                   #原来正则表达式并不是python的一部分。
                                                   #正则表达式是用于处理字符串的强大工具
                                                   #现在比较深刻的理解了正则表达式的强大
                                                   ##10day+：将提取出来的文字列表，转换成
                                                   #字符串文本
    
    words1 = jieba.cut(words)                      ##10day+jieba组件默认精确模式分词函数
    c = collections.Counter()                      #新建一个接收计数器的容器
    for x in words1:                               #设定每个元素都在文档列表里
        if len(x) > 1:                             #当统计长度大于2的元素时，装进计数器容器
            c[x] += 1                              #不断叠加，直到遍历完整个文档。

    count = int(input("您想统计前多少个词频最高词："))   #强制转换数据类型为整形
    list1 = c.most_common(count)   #调用最常见函数
    return list1











'''
    if not isinstance(text,str): #添加参数类型检查
        raise ValueError('输入的不是文本格式，请重新输入：')

    
    character_1 = []     #新建一个列表容器来接收筛选过后的中文字
    stat = {}            #新建一个字典来接收每个中文字出现的次数
    for line in y:
        line = line.strip()#把每行的首位空格去掉
        if len(line) == 0:       #如果首行是空的情况下，保留第一行
            continue
        for x in range(0,len(line)):            #每个字符都在每行里面
            if line[x] in ['，','。','\n','、']:    #将这些标点符号通过不断循环去除
                continue
            if not(line[x] in character_1):       #上一步遇到不是标点符号，就是中文字
                character_1.append(line[x])       #把这些中文字一个个放进新建的容器中
            if not(stat.__contains__(line[x])):   #如果这些键不在这个字典中，就把出现的放进去
                stat[line[x]] = 0                 #初始化值为零
            stat[line[x]] += 1                    #每放一个数量加1
    stat1 = sorted(stat.items(),key=lambda x:x[1],reverse=True)   #将字典内容按降序排列输出
    return stat1

#print(stats_text_cn(character))
'''


#ttt = '''
#今天，钉钉群里看到有位同学  
#可能是因为没有跟上训练营作业的进度，于是心生焦虑，
#出现了一点抱怨的情绪。
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#'''


def stats_text(y):              #通过程序分析之后，关键点事需要用一个函数来识别中英文,教练提示后用正则
    import re        #导入正则表达式（我不知道这样表达对不对，这个东西还没有学过，先用了）
    
    if not isinstance(text,str): #添加参数类型检查
        raise ValueError('输入的不是文本格式，请重新输入：')


    z = {}             #创建一个字典，用来接收中英文字典    
    a = re.findall(r'[\u4e00-\u9fa5]',y)     #只把中文找出来，具体意义还需要后期进行研磨                                        
    pass
    a = ''.join(a)     #找出来之后，为了调用上面的函数，再把它转变为字符串
    tt = dict(stats_text_cn(a))#调用函数后生成列表，然后再把列表转变为字典
    z.update(tt)               #利用update（）把字典加入到z字典中
    #return tt
    b = re.findall(r'[a-zA-Z]+',y)   #同理，只把英文单词找出来，切记一定要把表达式的 + ，加上，不然全部都变成字符
    b = ' '.join(b)      #与中文同理
    tt1 = dict(stats_text_en(b))    #与中文同理
    z.update(tt1)    #与中文同理
    d = sorted(z.items(),key=lambda x:x[1],reverse=True)  #再根据词频降序处理
    return d        #必须要有个值返回，不然无法输出
          

