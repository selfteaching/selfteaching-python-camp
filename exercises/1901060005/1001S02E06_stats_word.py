 
def stats_text_en(text):
    """count english words in the text"""
    t1=text.replace(',',' ').replace('.','').replace('!','').replace('*',' ').replace('-','').replace('?','')#将文档中的标点符号用空格代替
    t2=t1.split()#split()就是将一个字符串分裂成多个字符串组成的列表。
    wordcount={}#定义字典
    for i in t2:             
        wordcount[i]=t2.count(i)
    wordcount=sorted(wordcount.items(),key=lambda x:x[1],reverse=True)#字典参数和按值排序
    return wordcount
   
text='''Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. '''
print(stats_text_en(text))

def stats_text_cn(text):
   # '''count chinese words in the text'''
    t1=text.replace('，','').replace('。','').replace('!','').replace(' ','').replace('-','')
    #将文档中的标点符号用空格代替
    t2=' '.join(t1)#将列表转换为字符串
    wordcount={}#定义字典
    for i in t2:             
        wordcount[i]=t2.count(i)
    wordcount=sorted(wordcount.items(),key=lambda x:x[1],reverse=True)#字典参数和按值排序
    return wordcount
text ="""由于每个人的心灵品质和成长环境不同，在企业的发展过程中，多数人是在事上下功夫，少数人是在道德上下功夫，极少数人是在道上下功夫。"""
print(stats_text_cn(text))