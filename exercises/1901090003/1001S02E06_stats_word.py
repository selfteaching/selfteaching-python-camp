def stats_text_en(text):   #定义统计英文字符的函数
    word_str = text.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','')
    word_list = word_str.split()
    word_one = set(word_list)
    dict = {}
    for word in word_one:
        dict[word] = word_list.count(word)
        d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
        new_dict = {}
        for item in d_list:
            new_dict[item[0]] = item[1]
print(new_dict)

def stats_text_cn(text):        #定义统计英文字符的函数
    word_list = text
    word_one = set(word_list)   #对单词进行去重操作
    for x in word_list:
        if len(x) > 1 and x != '\r\n':
            Counter[x] +=1
    dict={}                     #构建词频词典   
    for word in word_one:
        dict[word] = word_list.count(word)
    d_list = sorted(dict.items(),key=lambda e:e[1], reverse=True)   #对于词频词典进行排序
    new_dict={}
    for item in d_list:
        new_dict[item[0]] = item [1]
    return new_dict           #返回按词频降序排列的数组
print(stats_text_cn(text))