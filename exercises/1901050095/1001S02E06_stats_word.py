t1 = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''

# 使用“字典”统计以上文本中出现的单词次数，并把结果从大到小输出
def stats_text_en(t1):   #定义函数，其中t1是可变的量
    t1 = t1.replace(',',' ').replace('.',' ').replace('--',' ').replace('*',' ').replace('!',' ') # 去标点
    t1 = t1.lower() # 全部换成小写
    t1 = t1.split() # 拆成字符串
    d = {} #定义字典
    for i in t1:
        count = t1.count(i) # 数数
        r1 = {i:count} # 单词在前，词频在后
        d.update(r1) #上传r1到d中去
    #print(d)
    print('\n按照出现次数降序输出所有单词:\n')
    d = sorted(d.items(),key=lambda x:x[1],reverse=True)
    # sorted(iterable,*,key=None,reverse=False) lambda是个特殊的定义函数，后面的是定义的表现形式，留待以后研究，reverse=True是颠倒的意思
    print(d)



#####################################################################################
t2='''学号：1901050095
姓名：陆永超
学习内容：day6掌握函数的用法（封装+调用）
1、封装day5的函数，封装其实很简单，就是定义（def）之后，直接运行（函数名+参数）。
2、知道了汉字字符在u4e00 到u9fa5之间，
学习用时：2天
收获总结：又反复看了数据容器的内容，把day5的第2个作业又思考了多次。
遇到的难点与问题（是否解决）：
1、关于文件的读取，还是没看明白，这次作业还是把样本文档放在程序文件中。希望后面会单独存放文本文件，并进行处理
2、辅导员发的视频很好。
'''

#该函数用于统计字符串中每个汉字出现的个数。需要输入字符串，输出的结果是按照降序排列的以中文汉字及其字频为元组的一个字典
def stats_text_cn(t2):
    #移除字符串头尾的空格和换行符号
    t2=t2.strip('\n+-*%.')
    #去除所有的标点符号
    biaodian='。，“”…，——，？：、！《》'
    for i in biaodian:
        t2=t2.replace(i,'')
    #到此text中应该只包含汉字，下面对汉字字符串进行统计,方法与统计单词基本一样，因为这里是统计中文汉字个数，所以每个汉字都是一个元素，
    #于是没有必要去将字符串再转换成一个单词列表
    char_dict={}
    for char in t2:
        if char in char_dict:
            count=char_dict[char]
        else:
            count=0
        count +=1
        char_dict[char]=count
    char_dict=sorted(char_dict.items(),key=lambda x:x[1],reverse=True)
    #输出最后的结果
    print('\n按照出现次数降序输出所有汉字:\n')
    print(char_dict)
 


def stats_text():   #将两个函数合并成一个函数。
                    #都有点怀疑python是不是太简单了，封装函数只是定义函数名+参数就行
    stats_text_en(t1)    #调用函数stats_text_en(t),参数为文本t1
    stats_text_cn(t2)    #调用函数stats_text_en(t),参数为文本t2

stats_text()    #运行函数，测试通过，完成day7第一个任务
