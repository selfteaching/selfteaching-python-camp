
import re

def stats_text_en(text):
    ''' count the number of every English word in a text '''
    if type(text) is not str:
        raise ValueError('request input sting type')
    else:
        text = text.lower()
        import re
        text_list = re.findall(r'\w+', text)
        text_set = set(text_list)
        d = {x:text_list.count(x) for x in text_set}
        d_list = [v for v in d.values()]
        d_list.sort(reverse=True)
        return d_list
    

def stats_text_cn(text):
    ''' count the number of every Chinese character in
    a text '''
    if type(text) is not str:
        raise ValueError('request input sting type')
    else:   
        import re
        text_list = re.findall(r'([\u4e00-\u9fff])',text)
        text_set = set(text_list)
        d = {x:text_list.count(x) for x in text_set}
        d_list = [v for v in d.values()]
        d_list.sort(reverse=True)
        return d_list


def stats_text(en_cn_text):
    ''' count the number of every Chinese character and English word in
    a text'''
    if type(en_cn_text) is not str:
        raise ValueError('request input sting type')
    else:
        import re
        stats_result = stats_text_en(en_cn_text) + stats_text_cn(en_cn_text) 
        stats_result.sort(reverse=True)
        return stats_result
    

