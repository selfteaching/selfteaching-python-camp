# 1. 统计中文汉字字频
# 2. 统计英文单词词频

# 统计中文汉字字频的函数
def stats_text_cn(text_cn): 

    if not isinstance(text_cn,str):  # 判断text_cn是否为字符串类型
        raise ValueError(f'输入的参数是{type(text_cn)}类型，不是字符串类型。') 
       
    d1 = {}  # 存储中文汉字的字典
    my_list = []  #定义列表

    # 清洗字符串，只保留汉字
    for s in text_cn: 
        if '\u4e00' <= s <= '\u9fff':   # 中文字符范围
            my_list.append(s)   # 把整理后的汉字，添加到列表中
            d1[s]=text_cn.count(s)  # 统计中文汉字词频
                
    d2 = sorted(d1.items(), key=lambda x:x[1], reverse=True)
    # 按照出现次数从大到小输出所有的单词及出现的次数,降序排列
    # key=lambda 元素: 元素[字段索引] ，此处 ，对第二个字段词频进行排序
    return d2 #   输出最终结果

# 统计英文单词词频的函数
def stats_text_en(text_en):  
    if not isinstance(text_en,str):  # 判断text_en是否为字符串类型
        raise ValueError(f'输入的参数是{type(text_en)}类型，不是字符串类型。') 
     
    t = text_en.replace(',',' ').replace('.',' ').replace('-',' ').replace('"',' ').replace('!',' ').replace('?',' ') 
    # 将非英文字符替换为空格

    d1 = {}  # 存储英文单词的字典
    my_list = ''   # 存储英文单词的字符串
    
    for s in t:  # 只保留英文单词
        if s.isascii():
            my_list += s

    t = my_list.lower()   # 把大写转换为小写        
    t = t.split()   # 以空格，把字符串内单词拆分为列表

    for i in t :    # 循环遍历列表中的单词
        d1.setdefault(i,t.count(i))   # 返回列表中单词出现的次数

    d2 = sorted(d1.items(), key=lambda x:x[1], reverse=True)
    # 按照出现次数从大到小输出所有的单词及出现的次数,降序排列
    # key=lambda 元素: 元素[字段索引] ，此处 ，对第二个字段进行排序

    return d2 #   输出最终结果    


def stats_text(text):

    if not isinstance(text,str):   # 判断text是否为字符串类型
        raise ValueError(f'输入的参数是{type(text)}类型，不是字符串类型。')   

    print("* 统计字符串样本中，中文汉字字频 *")
    print(stats_text_cn(text))  # 输出中文汉字字频
        
    print('-'*100)

    print("* 统计字符串样本中，英文单词词频 *")
    print(stats_text_en(text))  # 输出英文单词词频


