def states_text_en(text):
    s=text.replace(',','').replace('!','').replace('.','').replace('--','').replace('*','').lower()
    s1=s.split()
    dicts={}
    for i in s1:
        dicts[i]=s.count(i)
    s3=(sorted(dicts.items(),key=lambda x: x[1],reverse=True))
    print(s3)

states_text_en('''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.s
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
Namespaces are one honking great idea -- let's do more of those!''')


dict2={}  
def stats_text_cn(text):                   

    for i in text:
        if u'\u4e00' <= i <= u'\u9fa5':   
            dict2[i]=text3.count(i)
    s4=sorted(dict2.items(), key=lambda x: x[1],reverse=True)
    print(s4)

stats_text_cn('''
1.
The title track is a pointed meditation on a continent gone wrong. 
主打歌是对一个误入歧途的大陆的深刻沉思。
2.
A study of yoga leads naturally to meditation. 
学习瑜伽自然会发展到进行冥想。
3.
She found peace through yoga and meditation. 
她通过瑜伽和冥想找到了宁静。
''')

#对正则表达式不是很清楚，加强学习，加油！