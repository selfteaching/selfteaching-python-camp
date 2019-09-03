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

text_cn = '''
春眠不觉晓，
处处闻啼鸟。
夜来风雨声，
花落知多少。
'''

def stats_text_en(text):#定义函数，为文本中的单词计数
    n1=text.replace("\n","").replace(".","").replace("!","").replace("--","").replace("*","")#排除非单词字符
    words=n1.split(" ")#将字符串转换为列表
    dict={x:words.count(x) for x in words}#创建计数字典
    dict1=sorted(dict.items(), key=lambda d:d[1], reverse = True)#按照值降序排序
    print(dict1)

print(stats_text_en(text))

def stats_text_cn(text_cn):
    cn_characters=[]
    for character in text_cn:
         if '\u4e00' <= character <='\u9fff':
                cn_characters.append(character)
    dict={x:cn_characters.count(x) for x in cn_characters}
    dict1=sorted(dict.items(), key=lambda d:d[1], reverse = True)#按照值降序排序
    print(dict1)
print(stats_text_cn(text_cn))