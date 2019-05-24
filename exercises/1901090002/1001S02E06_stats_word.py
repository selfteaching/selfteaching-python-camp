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

text = """ Beautiful is better than ugly. 我从哪里来 1234567"""
print (stats_text_en(text))