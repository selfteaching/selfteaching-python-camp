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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''





def stats_text_en(text):              #定义函数
    text_a=text.replace(',',' ').replace('--',' ').replace('*',' ').replace('!',' ').replace('.',' ')     #删除标点符号
    text_b=text_a.lower()                                                                                 #建立字典
    text_c=text_b.split()
    word_dic={}
    for i in text_c:
        count=text.count(i)
        text_count={i:count}
        word_dic.update(text_count)
    
    word_dic1=sorted(word_dic.items(),key=lambda x:x[1],reverse=True)
    return word_dic1


print('统计参数中每个英⽂文单词出现的次数，最后返回⼀个按词频降序排列列的数组')
print(stats_text_en(text))



text_1 = '''
    最美的不是下雨天，是曾与你躲过雨的屋檐
　　
　　也许时间是一种解药，也是我现在所服下的毒药
　　
　  我一路向北，离开有你的季节，你说你好累，已无法再爱上谁。风在山路吹，过往的画面全都是我不对，细数惭愧，我伤你几回——《一路向北》
　　
　　翻着我们的照片，想念若隐若现，去年的冬天，我们笑得很甜。——《借口》
　　
　　转身离开，分手说不出来，海鸟跟鱼相爱，只是一场意外。——《珊瑚海》
　　
　　思绪不断阻挡着回忆播放，盲目的追寻仍然空空荡荡，灰蒙蒙的夜晚睡意又不知躲到哪去，一转身孤单已躺在身旁。——《回到过去》
　　
　　听妈妈的话别让她受伤，想快快长大才能保护她，美丽的白发幸福总发芽，天使的魔法温暖中慈祥。——《听妈妈的话》
'''

def stats_text_cn(text):
    text_cn1=text.replace(',','').replace('—',' ').replace('*',' ').replace('!',' ').replace('。',' ').replace('《','').replace('》','')
    
    word_list=[]
    for character in text_cn1:
        if u'\u4e00' <= character <= u'\u9fa5':
            word_list.append(character)
    
    word_dict={}
    set1=set(word_list)
    for character in set1:
        word_dict[character]=word_list.count(character)

    word_dict1=sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return word_dict1



print ('统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的数组')
print (stats_text_cn(text_1))