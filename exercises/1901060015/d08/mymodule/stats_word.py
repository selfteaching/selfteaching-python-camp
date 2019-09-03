
def stats_text_en(text):
    # 文章字符串前期处理
    strl_ist = text.replace('\n', '').replace('.', '').replace('!', '').replace('--', '').lower().split(' ')
    count_dict = {}
    #参数类型检查
    if not isinstance(text,(str)):
        raise TypeError('ValueError')
    # 如果字典里有该单词则加1，否则添加入字典
    for text in strl_ist:
        if text in count_dict.keys():
            count_dict[text] = count_dict[text] + 1
        else:
            count_dict[text] = 1
    #按照词频从高到低排列
    count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
    return count_list



def stats_text_cn(text):
    # 文章字符串前期处理
    strl_ist=[]
    for i in text:
        strl_ist.append(i)
    
    count_dict = {}
    #参数类型检查
    if not isinstance(text,(str)):
        raise TypeError('ValueError')
    # 如果字典里有该单词则加1，否则添加入字典
    for text in strl_ist:
        if text in count_dict.keys():
            count_dict[text] = count_dict[text] + 1
        else:
            count_dict[text] = 1
    #按照词频从高到低排列
    count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
    return count_list




def stats_text(text):
    #参数类型检查
    if not isinstance(text,(str)):
        raise TypeError('ValueError')
    text1=text[1:495]
    text2=text[495:2800]
    return stats_text_cn(text1)+stats_text_en(text2)












       



