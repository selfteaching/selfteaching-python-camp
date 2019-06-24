text1 = '''
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


#统计英文单词词频
#照搬了昨天的
def stats_text_en(text1):  #定义函数
    import re
    a = re.sub('[^a-zA-Z ]',' ',text1) #只保留英文
    b = a.split()  #切割成列表
    c = {}     #定义空字典
    for en in b:
        value = c.get(en,0) #获取单词统计数量
        value += 1 
        c[en] = value 
    d = sorted(c.items(), key=lambda x:x[1], reverse=True) #降序排序
    return d
print("打印英文单词词频结果为：")
print(stats_text_en(text1))



text2='''
1. 封装统计英⽂文单词词频的函数
1. 创建⼀一个名为 1001S02E06_stats_word.py 的⽂文件
2. 定义⼀一个名为 stats_text_en 的函数，函数接受⼀一个字符串串 text 作为参数
3. 实现该函数的功能（同 day5 任务 2）：统计参数中每个英⽂文单词出现的次数，最后返回⼀一个按词频降序排列列的数组
4. 为 stats_text_en 添加注释说明
2. 封装统计中⽂文汉字字频的函数
1. 在 1001S02E06_stats_word.py 中定义⼀一个名为 stats_text_cn 的函数，函数接受⼀一个字符串串 text 作为参数
2. 实现该函数的功能：统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的数组
3. 为 stats_text_cn 添加注释说明
3. 提交作业
1. 将本地仓库关于本次作业的变更更提交为⼀一个 commit
2. 通过 Github 桌⾯面客户端将本地电脑的变更更推送到⾃自⼰己账户下的作业仓库
3. 回到 Github ⾃自⼰己账户下的作业仓库⻚页⾯面，向远程公⽤用作业仓库的 master 分⽀支发起 Pull Request，在提交的 Pull Request 的标题（title）中填写⾃自⼰己所在的钉钉群名，
如示例例：【032901】⾃自学训练营 DAY1 ，并在评论（comment）中 @⾃自⼰己的助教（请向助教索要他的 Github ⽤用户名）提醒他检查作业
    '''


    
#统计中文汉字字频

def stats_text_cn(text2):  # 定义函数
    e = {} #定义空字典
    for ch in text2:
        if u'\u4e00' <= ch <= u'\u9fff': #中文字符范围，判断中文字符
            value =e.get(ch,0)  #获取汉字统计数量
            value += 1
            e[ch] =value
    f = sorted(e.items(), key=lambda item: item[1], reverse=True)  #降序排序
    return f
print("打印中文字符字频结果为：")
print(stats_text_cn(text2))      





