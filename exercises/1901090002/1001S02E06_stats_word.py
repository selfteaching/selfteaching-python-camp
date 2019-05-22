def stats_text_en(text):              #定义一个名为stats_text_en的函数,函数接受一个字符串text作为参数
    word = text.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','') #替换掉所有的符号
    word_list = word.split()    #按照空格将所有的单词分开
    word_one = set(word_list)   #对单词进行去重操作
    dict={}                     #构建词频词典   
    for word in word_one:
        dict[word] = word_list.count(word)
    d_list = sorted(dict.items(),key=lambda e:e[1], reverse=True)   #对于词频词典进行排序
    new_dict={}
    for item in d_list:
        new_dict[item[0]] = item [1]
    return new_dict             #返回按词频降序排列的数组
    
 # 以下作为输入的参数用以测试函数   
text = """ Beautiful is better than ugly. 我从哪里来 1234567
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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
Namespaces are one honking great idea -- let's do more of those!"""
print (stats_text_en(text))