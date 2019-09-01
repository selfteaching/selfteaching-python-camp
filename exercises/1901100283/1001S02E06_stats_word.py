#stats_text_en 封装统计英文单词词频的函数
def stats_text_en(text):
    a=text.split()
    x=[]
    for i in a:
        if i.isalpha() is True:
            x.append(i)
    n_dic={}
    for word in x:
        if word not in n_dic:
            n_dic[word]=1
        else:
            n_dic[word]=n_dic[word]+1
    sorted_dic=sorted(n_dic.items(),key=lambda n_dic:n_dic[1],reverse=True)
    return dict(sorted_dic)



#stats_text_cn 封装统计中文汉字字频的函数
def stats_text_cn(text):
    a=list(text)
    x=[]
    for i in a:
        if '\u4e00'<=i<='\u9fa5':
            x.append(i)
    n_dic={}
    for word in x:
        if word not in n_dic:
            n_dic[word]=1
        else:
            n_dic[word]=n_dic[word]+1
    sorted_dic=sorted(n_dic.items(),key=lambda n_dic:n_dic[1],reverse=True)
    return dict(sorted_dic)



