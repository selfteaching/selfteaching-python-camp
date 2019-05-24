import re
#(1)定义一个名为 stats_text_en 的函数
def stats_text_en(text):
    #(2)函数接受一个字符串 text 作为参数。如果不是字符串，则提示
    if not isinstance(text,str):
        return '请输入字符串'

    #(3)统计参数中每个英文单词出现的次数
    # 1.替换掉所有的符号
    word_str = text.replace(','," ").replace('.'," ").replace('!'," ").replace('*'," ").replace('--'," ")
    # 2.按照空格将所有的单词分割开

    word_str = re.sub(r'[^A-Za-z]',' ',word_str)
    word_list = word_str.split()


    # 3.对单词进行去重操作，作为字典的key
    word_one = set(word_list)
    # 4.构建一个词频字典
    dict = {}
    for word in word_one:
        dict[word] = word_list.count(word)
    # 5.对之前的词频字典按照value值进行排序
    d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d_list



#(1)定义一个名为 stats_text_cn 的函数
def stats_text_cn(text):
    #(2)函数接受一个字符串 text 作为参数。如果不是字符串，则提示
    if not isinstance(text,str):
        return '请输入字符串'

    # 1.替换掉所有的符号
    d = text.replace(',','').replace('-',' ').replace('.','').replace(':','').replace('《','').replace('’','').replace(';','').replace('"','').replace('!','').replace('?','').replace('》',' ').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace(' ','').replace("'",'')
    # 2.将上文中的字符串，用正则运算剔除所有英文字母单词，数字
    d = re.sub("[A-Za-z0-9]", "", d)
    #print(d)

    # 3.将字符串中的汉字去重，作为字典的key  
    #d_list = list(d)
    #print(d_list)
    #d_index = set(d_list)
    # 4.构造词频字典
    dict = {}
    for i in d:
        dict[i] = d.count(i)
    # 5.对之前的词频字典按照value值进行排序
    d = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d 





def stats_text(text):
        '''
        
        合并 英文词频 和 中文词频 的结果
        
        '''
        return stats_text_en(text)+stats_text_cn(text)
        

