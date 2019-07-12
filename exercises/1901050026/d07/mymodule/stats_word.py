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
import string #用import导入string模块

def stats_text_en(text):
    for x in string.punctuation:#用string模块中的punctuation功能检查标点符号并用空格代替
	    text1=text.replace(x,"")
    text2=text1.split() #以空格拆分为独立单词

    dic={}
    for i in text2:  #将字符串转换为字典
        count=text2.count(i)
        r1={i:count}
        dic.update(r1)
    dic1=sorted(dic.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序
    return(dic1)
print(stats_text_en(text1))  #调用函数并打印结果


########################


#2.封装统计中文汉字字频的函数 
text_1 = '''                       
Having completed 90% of the marathon, the runner pushed through the pain to make it to the end.跑完了马拉松90%的赛程之后，这名运动员顶着痛苦，坚持跑到了终点。The mountaineer had to push through the pain to complete the climb to the summit.这个登山者挺过痛苦，爬上了山顶。If you push through the pain and complete the workout, you’ll feel really good about yourself.如果你能挺过痛苦并完成训练，你的自我感觉会很好。
'''

def stats_text_cn(text):    #定义检索中文函数
    cndic={} 
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':#判断是不是中文
            count = text.count(i)
            cndic2 = {i:count}
            cndic.update(cndic2)
    cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True) 
    return cndic
print(stats_text_cn(text_1)) #调用函数并打印结果







def stats_text(text) :
    ''' 合并英汉词频统计 '''

    return stats_text_en(text)+stats_text_cn(text)



