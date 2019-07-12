import re 

def stats_text_en(t_en): 
    if not isinstance(t_en,str):
        raise ValueError('输入的不是文本格式，请重新输入：') #isinstance(object, classinfo) 判断函数 object，对象   classinfo，类型
    '''英文词频统计'''
    a = t_en.replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace('--',' ')
    a = a.lower()
    a = re.sub("[^A-Za-z]", " ", a)
    a = a.split() 
    b = {}
    for i in a:
        count =  a.count(i)
        r1 = {i:count} 
        b.update(r1)
    c = sorted(b.items(),key=lambda x:x[1],reverse=True) 
    print('英文单词统计频率如下： \n',c)
    

def stats_text_cn(t_cn):
    if not isinstance(t_cn,str):
        raise ValueError('输入的不是文本格式，请重新输入：')
    '''中文词频统计'''
    d = t_cn.replace(',','').replace('-',' ').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace(' ','')
    d = re.sub("[A-Za-z0-9]", "",d) 
    e = {}
    for j in d:
        count = d.count(j)
        r2 = {j:count}
        e.update(r2)
    f = sorted(e.items(),key=lambda x:x[1],reverse=True)
    print('中文单字统计频率如下： \n',f)

def stats_text(en_cn):
    '''中英文词频统计'''
    if not isinstance(en_cn,str):
       return (stats_text_cn(en_cn)+stats_text_en(en_cn))
    else:
        raise ValueError('输入的不是文本格式，请重新输入：')
   
    