def stats_text_en(text):#定义函数
    t1= text.split()
    print (t1)
    dict = {}#统计单词出现次数
    for token in t1:
        dict[token] = dict.get(token, 0) + 1
    print(dict)
    list1= sorted(dict.items(),key=lambda x:x[1],reverse=True) #降序排列
    print(list1)
    return
#给参数赋值
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
stats_text_en(text) #调用定义函数




def stats_text_cn(text):    #定义检索中文函数
    dict={}
    for i in text:
        if u'\u4e00' <= i <= u'\u9fa5': #提取中文汉字，\u是unincode编码，u4e00是十六进制表达值
            dict[i]=text.count(i)
        list2= sorted(dict.items(),key=lambda x:x[1],reverse=True) #降序排列
    print(list2)
    return

text1= '''                       
The Zen of Python, by Tim Peters
美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
可读性计数.
Special cases aren't special enough to 打破规则.
即使练习会使得不再纯粹.
但错误不应该用沉默来掩盖.
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
有且只有一个办法.
Although that way may not be obvious at first unless you're Dutch.
尝试总比从未试过要强.
Although never is often better than *right* now.
如果执行很难被解释，那将是一个很糟的想法.
如果执行很容易解释，这会是一个好点子.
Namespaces are one honking great idea -- 让我们继续为之努力!
'''
stats_text_cn(text1)#调用定义函数
