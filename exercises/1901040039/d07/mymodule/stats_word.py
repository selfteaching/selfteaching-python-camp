
# 此文件用函数封装统计词频及排序的操作

def stats_text_en(list_a,dic_a) :
    """通过dictionary统计list_a中每个英文单词出现的次
    数，并返回该结果"""

    # 通过dictionaries 进行统计中文词频
    for i in range(len(list_a)) :
        if list_a[i] in dic_a :
            dic_a[list_a[i]] += 1
    return dic_a




def stats_text_cn(list_a,dic_a) :
    """通过dictionary统计list_a中每个中文单词出现的次数
    ，并返回该结果"""

    # 通过dictionaries 进行统计英文词频
    for i in range(len(list_a)) :
        if list_a[i] in dic_a :
            dic_a[list_a[i]] += 1
    return dic_a


def stats_text(text) :
    """将text中的字符串放入list容器，分别调用
    stats_text_cn、stats_text_en函数输出词频统计结果"""
    list_a = []
    list_b = []
    dict_c = {}
    j = 0
# 将text文件转为list结构
    for i in range(len(text)) :
        if (text[i] >= '\u4e00') and (text[i] <= '\u9fa5') : #将中文单词放入list和dictionary
            list_a.append(text[i])
            j = i + 1
            if text[i] not in dict_c :
                dict_c[text[i]] = 0
        elif (ord(text[i]) not in range(65,91)) and (ord(text[i]) not in range(97,123)) and (text[i] != "\'") :#将英文单词放入list和dictionary
            if i == j :
                j += 1
            else :
                list_b.append(text[j:i])
                if text[j:i] not in dict_c :
                    dict_c[text[j:i]] = 0
                j = i + 1
        elif i == (len(text)-1) : #当末尾是字母或'时，增加最后一个英文单词
            list_b.append(text[j:i+1])
            if text[j:i+1] not in dict_c :
                    dict_c[text[j:i+1]] = 0
    if len(list_a) == 0  and len(list_b) == 0 :
        return
    print('列表：\n' 'list_a：', list_a,'\n\n' 'list_b：',list_b, end = '\n\n')

    #分别调用两个函数统计词频
    stats_text_cn(list_a,dict_c)
    stats_text_cn(list_b,dict_c)

    #排序输出
    return print('排序后：', sorted(dict_c.items(), key = lambda x:x[1], reverse = True), end = '\n\n') 