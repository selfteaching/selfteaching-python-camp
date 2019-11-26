#1.封装统计英文单词词频的函数
text1='''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
最美的不是下雨天，是曾与你躲过雨的屋檐
也许时间是一种解药，也是我现在所服下的毒药
我一路向北，离开有你的季节，你说你好累，已无法再爱上谁。风在山路吹，过往的画面全都是我不对，细数惭愧，我伤你几回——《一路向北》
翻着我们的照片，想念若隐若现，去年的冬天，我们笑得很甜。——《借口》
转身离开，分手说不出来，海鸟跟鱼相爱，只是一场意外。——《珊瑚海》
思绪不断阻挡着回忆播放，盲目的追寻仍然空空荡荡，灰蒙蒙的夜晚睡意又不知躲到哪去，一转身孤单已躺在身旁。——《回到过去》
听妈妈的话别让她受伤，想快快长大才能保护她，美丽的白发幸福总发芽，天使的魔法温暖中慈祥。——《听妈妈的话》
'''

def stats_text_en(text):
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
print(stats_text_en(text1))  #调用函数并打印结果

  

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
    cndic={} 
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':#判断是不是中文
            count = text.count(i)
            cndic2 = {i:count}
            cndic.update(cndic2)
    cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True) 
    return cndic
print(stats_text_cn(text_1)) #调用函数并打印结果

def stats_word(text): #定义函数，实现统计汉字和英文单词出现次数
    print(stats_text_en(text))
    print(stats_text_cn(text))
stats_word(text_1)