
def stats_text_en(text):
    #删除非单词符号
    replace_text = text.replace('--','').replace(',','').replace('.','').replace('*','').replace('!','')
    
    #对字符串进行切片
    split_text = replace_text.split()
    #建立一个字典
    dict_text = {}
    for word in split_text:
        if word not in dict_text:
            dict_text[word] = 1
        else:
            dict_text[word] +=1
    #排序
    return sorted(dict_text.items(),key = lambda d: d[1],reverse = True)
    #return sorted(frequency.items(), key=lambda d: d[1], reverse=True)



def stats_text_cn(text):
    #删除非单词符号
    replace_text = text.replace('；','').replace('，','').replace('。','').replace('？','').replace('!','').replace('：','')
    
    #对字符串进行切片
    split_text = replace_text.split()
    #建立一个字典
    dict_text = {}
    for word_cn in split_text:
        if word_cn not in dict_text:
            dict_text[word_cn] = 1
        else:
            dict_text[word_cn] +=1
    #排序
    return sorted(dict_text.items(),key = lambda d:d[1],reverse = True)


text = "为蛇口蛇设阿拉的喝口茶"
#print(stats_text_cn(text))

text_en = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
'''
print(stats_text_en(text_en))
    

def str_count2(str):
    for s in str:
        # 中文字符范围
        if '\u4e00' <= s <= '\u9fff':
            print(s, end="\t")


str = "为蛇口蛇设阿拉的喝茶"
print(str_count2(str))



