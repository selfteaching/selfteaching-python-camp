def stats_text_en(text):    # 统计文本中英文单词出现的次数，并按词频降序排列，返回数组
    text1=text.replace(',','').replace('.','').replace('!','').replace('*','').replace('-','').replace('?','') #去标点
    text2=text1.lower().split()   #拆分并转字符串
    dic={}#定义字典
    for i in text2:    
        if i.isascii():         
            dic[i]=text2.count(i)
    dic2=sorted(dic.items(),key=lambda x:(x[1],x[0]),reverse=True)     #对字典按值（value）进行从大到小排序,若值相同则按键字母排序
    return dic2


def stats_text_cn(text):    # 统计文本中中文汉字出现的次数，并按词频降序排列，返回数组
    text1=text.replace('，','').replace('。','').replace('!','').replace('*','').replace('-','').replace('?','') #去标点
    text2=''.join(text1)#将列表转换为字符串
    dic={}#定义字典
    for i in text2:
        if u'\u4e00' <= i <= u'\u9fa5': #提取中文汉字             
            dic[i]=text2.count(i)
    dic2=sorted(dic.items(),key=lambda x:(x[1],x[0]),reverse=True)#字典参数和按值排序
    return dic2
# text ='''天下只有两种人。比如一串葡萄到手，一种人挑最好的先吃，另一种人把最好的留到最后吃。照例第一种人应该乐观，因为他每吃一颗都是吃剩的葡萄里最好的；第二种人应该悲观，因为他每吃一颗都是吃剩的葡萄里最坏的。不过事实却适得其反，缘故是第二种人还有希望，第一种人只有回忆。'''
# print('测试文本：\n',text)
# print('统计如下：\n',stats_text_cn(text))

def stats_text(text):   # 分别调用stats_text_en和stats_text_cn,输出合并词频统计结果
    print(stats_text_en(text),'\n',stats_text_cn(text))