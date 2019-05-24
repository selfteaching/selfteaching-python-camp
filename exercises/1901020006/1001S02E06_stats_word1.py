# 封装统计英文单词词频的函数
# 1定义一个名为 stats_text_en 的函数
def stats_text_en(text):
    if not isinstance(text,str):
        return '请输入字符串'
    

    # 2.统计参数中每个英文单词出现的次数
    # 3.替换掉所有的符号
    text1 = text.replace(',','').replace('.','').replace('--','').replace('!','').replace('*','')
    # 4.按照空格把所有单词分隔开
    text2 = text.split()
    # 5.构建一个词频字典
    dict = {}
    for i in text2:
        j=text2.count(i)
        dict2 = {i:j}
        dict.update(dict2)
    # 6.对之前的词频字典按照value值进行排序
    dict3 = sorted(dict.items(),key=lambda x:x[1],reverse=True)
    print(dict3)
        

#(1)定义一个名为 stats_text_cn 的函数
def stats_text_cn(text):
    #(2)函数接受一个字符串 text 作为参数。如果不是字符串，则提示
    if not isinstance(text,str):
        return '请输入字符串'

    # 1.替换掉所有的符号
    d = text.replace(',','').replace('-',' ').replace('.','').replace(':','').replace('《','').replace(';','').replace('"','').replace('!','').replace('?','').replace('》',' ').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace(' ','').replace("'",'')
    # 2.将上文中的字符串，用正则运算剔除所有英文字母单词，数字
    d = re.sub("[A-Za-z0-9]", "", d)
    print(d)

    # 3.将字符串中的汉字去重，作为字典的key  
    d_list = list(d)
    print(d_list)
    d_index = set(d_list)
    # 4.构造词频字典
    dict = {}
    for i in d_index:
        dict[i] = d_list.count(i)
    # 5.对之前的词频字典按照value值进行排序
    d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d_list 