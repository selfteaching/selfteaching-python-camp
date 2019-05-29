
def stats_text(text):      
    if (text >= '\u4e00' and text <= '\u9fa5'):
        return stats_text_cn(text)
    else:
        return stats_text_en(text)
   
 #定义一个stats_text(text)的函数，通过判断，选择调用对应的函数
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
    
from collections import Counter
def stats_text_cn(text):              #定义一个名为stats_text_en的函数,函数接受一个字符串text作为参数
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


text = """实现该函数的功能:统计参数fadf adf adfd 中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的数组组"""
print(stats_text(text))