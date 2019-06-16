#统计每个英文单词出现的次数，返回一个按词频降序排列的数组
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

#作业1
#函数 stats_text_en(text) : 接受字符串text，统计每个词出现的次数，返回按词频降序排列的数组

#定义函数stats_text_en()，参数为text
def stats_text_en(text):
    #文本中的符号‘，’，‘--’，‘！’，‘*’用空格代替
    T1=text.replace(',',"").replace('--',"").replace('!',"").replace('*',"")
    #把文本“分裂”成一个个单词（列表）
    T1=T1.split()
    #列表T2：由单词组成
    T2=[]
    for x in T1:
        if x.isalpha:
            T2.append(x)
    
    #字典dict
    #最初为空字典，随后一对一对的增加单词和出现的次数
    dic={}
    for x in T2:
        y = T2.count(x)
        dict1 = {x:y}
        dic.update(dict1)
    #按照出现次数的多少（降序）排列
    dict2=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    return(dict2)

#调用函数stat_text_en()，参数为text1文本
print(stats_text_en(text1))

#作业2
text2='''
Pride and Prejudice is kind of a literary Rosetta Stone, the inspiration, basis, and model for so many modern novels. You’re probably more familiar with its plot and characters than you think. For a book written in the early 19th century, it’s modernity is surprising only until you realize that this is the novel that in many ways defined what a modern novel is.
《傲慢与偏见》可以说是文学界的一块罗塞塔石碑，同时也是许多现代小说的模板，所以你对其中的情节和人物可能比你自己想象中要熟悉。作为一本写于19世纪的书，它的现代性是非常惊人的，而你稍作了解之后就会知道，这是因为现代小说在很大程度上就是被这本书定义的。
'''

#定义函数stats_text_cn
def stats_text_cn(text):
    dicc={} 
    for x in text:
        if u'\u4e00' <= x <= u'\u9fff':#判断是不是中文
            y = text.count(x)
            dicc1 = {x:y}
            dicc.update(dicc1)
    dicc2=sorted(dicc.items(),key=lambda item:item[1],reverse = True) 
    return dicc2
print(stats_text_cn(text2)) #调用函数并打印结果





 




    

        


