'''
代码试验区，以下为试验成功代码：
d7 模块的使用

import re
def stats_text_en(text):  #定义函数
    text_1 = re.sub(r'[\W\u4e00-\u9fa5]',' ',text) #去除中文、非字符，将其转换为空格。
    text_1 = text_1.lower() #转换为小写
    textlist_1 = text_1.split()#将段落转换为列表
    dict1 = {} 
    for i in textlist_1:
        num= textlist_1.count(i)
        r1 = {i:num}
        dict1.update(r1)
        dict2=sorted(dict1.items(),key = lambda dict_items:dict_items[1], reverse=True)
    return(dict2)

'''

cn=int(input())
print(cn)