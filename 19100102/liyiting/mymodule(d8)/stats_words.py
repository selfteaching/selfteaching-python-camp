

def stats_text_en(text):
    dict1 = {}
    import re
    ''' 保留英文单字 '''
    en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
    list1 = re.findall(en_pattern, text)
    
    
    #print(list)
    for i in list1:
        ''' 统计次数 '''
        num = list1.count(i)
        '''使用setdefault给list中的词按次序添加键，并设定值为num'''
        dict1.setdefault(i,num)
        '''按照每个词的num作为key值排序'''
        tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)

   
    dict2 = {}

    '''遍历tup1'''
    for i in tup1:
        dict2[i[0]] = dict1[i[0]]
    return dict2


def stats_text_cn(text):
    dict1 = {}
    import re
    ''' 保留中文单字 '''
    cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
    list1 = re.findall(cn_pattern, text)
    
    
    #print(list)
    for i in list1:
        num = list1.count(i)
        dict1.setdefault(i,num)
        tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)

    
    dict2 = {}

    '''遍历tup1'''
    for i in tup1:
        dict2[i[0]] = dict1[i[0]]
    return dict2

'''定义stats_text函数'''
def stats_text(text):
    return (stats_text_en(text),stats_text_cn(text))
    
def stats_text(text):
    '''使用isinstance函数验证输入的参数类型是否为str'''
    if isinstance(text, str) != True: 
        '''用raise语句来引发异常'''
        raise ValueError
    else: 
        return (stats_text_en(text),stats_text_cn(text))