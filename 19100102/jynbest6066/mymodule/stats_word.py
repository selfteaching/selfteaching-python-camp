
def stats_text_en(text):
    dict1 = {}
    import re
    ''' 保留英文单字 '''
    en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
    list1 = re.findall(en_pattern, text)
    
    import collections
    '''调用collections的Counter函数'''

    #cnt = collections.Counter()
    #for word in list1:
        #cnt[word] += 1
    '''添加一个int类型变量count'''
    count = int(100)
    list2 = collections.Counter(list1).most_common(count)
    
    return list2


def stats_text_cn(text):
    dict1 = {}
    import re
    ''' 保留中文单字 '''
    cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
    list1 = re.findall(cn_pattern, text)
    
    import collections
    '''调用collections的Counter函数'''
    #cnt = collections.Counter()
    #for word in list1:
        #cnt[word] += 1

    '''添加一个int类型变量count'''
    count = int(100)
    list2 = collections.Counter(list1).most_common(count)
    
    return list2


def stats_text(text):
    '''使用isinstance函数验证输入的参数类型是否为str'''
    if isinstance(text, str) != True: 
        '''用raise语句来引发异常'''
        raise ValueError
    else: 
        return (stats_text_en(text),stats_text_cn(text))
