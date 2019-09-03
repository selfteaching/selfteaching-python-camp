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
text1 = text.replace('.','').replace(',','').replace('!','').replace('--','').replace('*','').replace('\n',' ').lower().split(" ")  # 消除标点符号,小写转换。
def stats_text_en(text):        #定义函数
    dict1 = {}              #dict 为字典类 
    for i in text1:     
        if i in dict1:      #即查找出同时存在于text1与dict1中的单词
            dict1[i] += 1   #统计它的出现次数
        else:               
            dict1[i] = 1    
    result = sorted(dict1.items(),key=lambda x:x[1],reverse=True)           
    return result
print(stats_text_en(text1))

#https://github.com/selfteaching/selfteaching-python-camp/issues/1568 不明白就去这

text3 = '''
1.
The title track is a pointed meditation on a continent gone wrong. 
主打歌是对一个误入歧途的大陆的深刻沉思。
2.
A study of yoga leads naturally to meditation. 
学习瑜伽自然会发展到进行冥想。
3.
She found peace through yoga and meditation. 
她通过瑜伽和冥想找到了宁静。
'''

dict2={}  
def stats_text_cn(text):                   #引用字典
    for i in text3:
        if u'\u4e00' <= i <= u'\u9fa5':   #提取中文汉字   
            dict2[i]=text3.count(i)
    return dict2
frequency = stats_text_cn(text)
print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))
print(dict2)