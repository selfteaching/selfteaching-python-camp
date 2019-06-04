#1.封装统计英文单词词频的函数
text1='''
Remember the day I borrowed your brand new car and dented it？
I thought you'd kill me
But you didn't.
And remember the time I dragged you to the beach
And you said it would rain, and it did?
I thought you'd say, "I told you so."
But you didn't.

Do you remember the time I flirted with all the guys?
To make you jealous, and you were？
I thought you'd leave，
But you didn't.
 Do you remember the time I spilled strawberry pie all over your car rug?
I thought you'd hit me.
But you didn't.

And remember the time I forgot to tell you the dance was formal
And you showed up in jeans？
I thought you'd drop me.
But you didn't.

Yes, there were lots of things you didn't do.
But you put up with me, and loved me, and protected me.
There were lots of things I wanted to make up to you when you returned from Vietnam.
But you didn't.
'''

def stats_text_en(text):
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    for x in text:
        for x in ',','.','?','"','!','，','。','？','！','：','「','」':
	        text=text.replace(x,"")
    text2=text1.split() #以空格拆分为独立单词

    for i in text2:
        if u'\u4e00' <= i <= u'\u9fff':#判断是不是中文
            text2.remove(i) #将列表中中文删除

    dic={}
    for i in text2:  #将字符串转换为字典
        count=text2.count(i)
        r1={i:count}
        dic.update(r1)
    dic1=sorted(dic.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序
    return(dic1)
#print(stats_text_en(text1))  #调用函数并打印结果

  

#2.封装统计中文汉字字频的函数 
text_1 = '''                       
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

def stats_text_cn(text):    #定义检索中文函数
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    cndic={} 
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':#判断是不是中文
            count = text.count(i)
            cndic2 = {i:count}
            cndic.update(cndic2)
    cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True) 
    return cndic
#print(stats_text_cn(text_1)) #调用函数并打印结果

def stats_word(text): #定义函数，实现统计汉字和英文单词出现次数
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    print(stats_text_en(text))
    print(stats_text_cn(text))
#stats_word(text_1)