


# 封装统计单词词现的次数
def stats_text_en(text):
    text1 = text.replace(',', ' ').replace('.', ' ').replace('--', ' ').replace('!', ' ').replace('*', ' ')#清除不必要的字符
    text2 = text1.split()
    text3 = set(text2)#去重处理
    dict2 = {}
    for i in text3:
        j = text.count(i)#单词计数
        dict1 = {i: j}
        dict2.update(dict1)#创建新字典
    dict3 = sorted(dict2.items(), key=lambda x: x[1], reverse=True)#按照值进行排序
    return dict3#返回值
# print(stats_text_en(text))  #打印测试


def stast_text_cn(text_cn):
    text = text_cn.replace('。', '').replace('，', '').replace('-', '').replace('*', '').replace('!', '').replace('\n','').replace(' ','')
    d3 = {}
    for i in text:
        count = text.count(i)
        dict2 = {i:count}
        d3.update(dict2)
    d4 = sorted(d3.items(),key = lambda x:x[1],reverse = True)
    return d4

def stats_text(text):
    #中英文词频统计
    return (stast_text_cn(text)+stats_text_en(text))