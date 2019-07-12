def stats_text_en(text):
    punctuation = [',','.','--','*','!','?','\n']
    for i in punctuation:
        text = text.replace(i," ") #将标点符号替换为空格
    text = text.lower()            #全部转换为小写
    text = text.replace('\'re', ' are') #将缩写替换为完整单词
    text = text.replace('aren\'t', ' are not')
    text = text.replace('it\'s', 'it is')
    text = text.replace('let\'s', 'let us')
    list1 = text.split(' ') #将string转换为列表，以空格分割
    for i in list1:
        if '' in list1:
            list1.remove('') #去除列表中空字符
    word_count = {}
    for word in list1:
        if not word in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    word_count = sorted(word_count.items(), key = lambda item :item[1],reverse=True)
    return word_count
 
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
print(stats_text_en(text))