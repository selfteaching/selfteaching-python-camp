text=  '''                       
"Her eyes beginning to water, she went on,
"So I would like you all to make me a promise:
from now on, on your way to school，
or on your way home, find something beautiful
to notice. It doesn' t have to be something you
see -it could be a scent perhaps of freshly
baked bread wafting out of someone 's house,
or it could be the sound of the breeze
slightly rustling the leaves in the trees,
or the way the morning light catches one
autumn leaf as it falls gently to the ground.
Please, look for these things, and remember them."
　　她的眼睛开始湿润了，她接着说因此我想让你们每个人答应我:
从今以后，在你上学或者放学的路上，要发现一些美丽的事物。
它不一定是你看到的某个东西——它可能是一种香味——
也许是新鲜烤面包的味道从某一座房里飘出来，也许是微风轻拂树叶的声音，
或者是晨光照射在轻轻飘落的秋叶上的方式。请你们寻找这些东西并且记住它们吧。 
'''
import re
import collections
import jieba #结巴中文分词
count=int()
def stats_text_en(text,count):
    if type(text) == str: 
        b=re.sub(r'[^A-Za-z]',' ',text) 
        list1=b.split() 
        return(collections.Counter(list1).most_common(count)) 
    else:
        raise ValueError('文本为非字符串')

def stats_text_cn(text,count):
    if not isinstance(text,str): 
        raise ValueError('文本为非字符串') 
    p=re.compile(u'[\u4e00-\u9fa5]') 
    a=re.findall(p,text) 
    str2=''.join(a)           
    seg_list = jieba.cut(str2,cut_all=False) #jieba.cut返回的结构是一个可迭代的生成器generator
    newlist=[]
    for i in seg_list:
        if len(i) >= 2:
            newlist.append(i)
    return(collections.Counter(newlist).most_common(count)) 

def stats_text(text,count):     
    if not isinstance(text,str):
        raise ValueError('文本为非字符串')
    stats_text_cn(text,count) 
    stats_text_en(text,count) 
stats_text(text,count)
