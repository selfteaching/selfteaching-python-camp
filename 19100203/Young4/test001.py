import re
def stats_text_en(text):  #定义函数
    text_1 = re.sub(r'[\W\u4e00-\u9fa5]',' ',text) #不是字符的，都转换为空格。主要去除标点符号
    text_1 = text_1.lower() #转换为小写
    textlist_1 = text_1.split()#将段落转换为列表
    dict1 = {} 
    for i in textlist_1:
        num= textlist_1.count(i)
        r1 = {i:num}
        dict1.update(r1)
        dict2=sorted(dict1.items(),key = lambda dict_items:dict_items[1], reverse=True)
    return(dict2)



text = '''
abc,frd,hugggv,我是一串字母，想把我分开？
'''

print(stats_text_en(text))