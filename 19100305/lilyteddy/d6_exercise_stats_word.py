def  stats_text_en(text) :
    text1=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ') #替换分隔符为空格
    text2=text1.split( )#切成单词
    #定义一个dict
    dict={}
    #将x中的每一个单词进行判断，无则赋值，有则赋值+1
    for it in text2:
        
         #是英文的进入下一步处理
        if all(ord(c)<128 for c in it):
            if it not in dict:
                dict[it] = 1
            else: dict[it] += 1
    #排序，按值，倒序
    dict = sorted(dict.items(),key=lambda x:x[1],reverse=True)
    #返回处理好的dict
    return dict


x = '''
The Zen of Python, by Tim Peters 小猪
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



print(stats_text_en(x))




#任务2 中文字符排序

def  stats_text_cn(text) :
    text2=list(text)#切成一个一个字
    #定义一个dict
    dict={}
    #将x中的每一个单词进行判断，无则赋值，有则赋值+1
    for it in text2:
        #是中文的进入下一步处理
        if u'\u4e00'<= it<= u'\u9fff':
            if it not in dict:
                dict[it] = 1
            else: dict[it] += 1
    #排序，按值，倒序
    dict = sorted(dict.items(),key=lambda x:x[1],reverse=True)
    #返回处理好的dict
    return dict

y= '''
    将x中的每一个单词进行判断，无则赋值，有则赋值
    '''
print(stats_text_cn(y))