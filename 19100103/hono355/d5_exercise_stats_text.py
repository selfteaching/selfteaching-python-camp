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
def sort_en_word(text):
#统计字符串样本中英文单词出现的次数
    text_en = "".join(i for i in text if ord(i) < 256)     #分离出文本中的英文
    text = text_en
    for i in '*,，。.-!、？！“”""?「」':
        text = text.replace(i,'')#去掉标点等符号
    text = text.lower()#将所有大写变成小写，以便后面单词计数
    textlist = text.split()#将text的字符串以空格为分隔符分割成字符串并赋值
    
    word_dict = {}
    for i in textlist:#统计各个单词出现的次数
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] += 1
    
    sort_en_word = sorted(word_dict.items(),key=lambda item:item[1],reverse=True)#按单词出现次数降序排序
    
    print('sort_en_word => ', sort_en_word)
    return(sort_en_word)
    
sort_en_word(text)
'''
word_dict.items()是将word_dict转换为可迭代对象，items()方法将字典的元素转化为了元组，
而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数（如果写作
key=lambda item:item[0]的话则是选取第一个元素作为比较对象，也就是key值作为比较对象），
采用这种方法可以对字典的value进行排序。注意排序后的返回值是一个list，而原字典中的名值对
被转换为了list中的元组。reverse=True表示降序排列。
'''