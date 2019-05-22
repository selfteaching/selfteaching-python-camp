
text_en= '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
text_cn= '''
三大人生之坑
第一，莫名其妙地凑热闹。
第二，心急火燎地随大流。
第三，操碎了别人的心。
'''
def stats_text_en(n): 
    word_dict={}
    import string
    word_lst=n.translate(str.maketrans('','',string.punctuation))   #去除标点符号
    words=word_lst.split()
    for item in words:
        if  item not in word_dict:
            word_dict[item] = 1
        else:
            word_dict[item] += 1
    return sorted(word_dict.items(),key=lambda item:item[1], reverse=True)
        # print(key)
    

def stats_text_cn(n): 
    word_dict={}
    word_lst=[]
    for line in n:
        for char in line:
            word_lst.append(char)
    word_text=' '.join(word_lst)
    import re        
    words=re.findall('[\u4e00-\u9fa5]',word_text) #去除标点符号,只保留汉字
    for item in words:
        if  item not in word_dict:
            word_dict[item] = 1
        else:
            word_dict[item] += 1
    return sorted(word_dict.items(),key=lambda item:item[1], reverse=True)
        # print(key)

print(stats_text_en(text_en))
# print(stats_text_cn(text_cn))
