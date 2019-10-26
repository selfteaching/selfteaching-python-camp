

#\u4e00-\u9fa5 	汉字的unicode范围
#\u0030-\u0039 	数字的unicode范围
#\u0041-\u005a 	大写字母unicode范围
#\u0061-\u007a 	小写字母unicode范围

from collections import Counter

def stats_text_en(text,count):              #定义函数
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    text_d = []
    text_a=text.replace(',',' ').replace('--',' ').replace('*',' ').replace('!',' ').replace('.',' ').replace('—',' ').replace('。',' ').replace('《','').replace('》','').replace('，',' ')     #删除标点符号
    text_b=text_a.lower()                                                                          
    text_c=text_b.split()
    for i in text_c:
        if u'\u0041' <= i <= u'\u005a':
            text_d.append(i) 
        elif u'\u0061' <= i <= u'\u007a':
            text_d.append(i)
    return Counter(text_d).most_common(count)  






def stats_text_cn(text,count):
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    text_cn1=text.replace(',',' ').replace('--',' ').replace('*',' ').replace('!',' ').replace('.',' ').replace('—',' ').replace('。',' ').replace('《','').replace('》','') 
    
    word_list=[]
    for character in text_cn1:
        if u'\u4e00' <= character <= u'\u9fa5':
            word_list.append(character)
    return Counter(word_list).most_common(count)
    





def stats_word(text,count): #定义函数，实现统计汉字和英文单词出现次数
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    
    return stats_text_en(text,count) + stats_text_cn(text,count)








