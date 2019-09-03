
# 此文件用函数封装统计词频及排序的操作
import collections as coll
import jieba

def stats_text_cn(text, common_t = None) :
    """通过counter统计text中每个中文单词出现的次数，并返回counter对象"""

    # 参数类型异常检测
    try :
        if type(text) != type("") :
            raise ValueError('That was no valid str')
    except ValueError :
        return 
    finally :
        print()

    # 通过jieba进行分词
    seg_list = '/'.join(jieba.cut(text, cut_all = False))

    # 通过counter进行统计中文词频
    counter_a = coll.Counter()
    list_a = []
    for i in range(len(seg_list)) :
        if i == (len(seg_list)-1) :
            list_a.append(seg_list[i])
            counter_a["".join(list_a)] += 1
        elif seg_list[i] != '/' :
            if (seg_list[i] >= '\u4e00') and (seg_list[i] <= '\u9fa5') : #此判断主要为了避免出现分词后形成 "/天气good/ 的情况
                list_a.append(seg_list[i])
        else :
            if len(list_a) != 0 :
                counter_a["".join(list_a)] += 1
                list_a = []

    print('中文排序后：', counter_a.most_common(common_t), end = '\n\n')
    return counter_a.most_common(common_t)




def stats_text_en(text, common_t = None) :
    """通过counter统计text中每个英文单词出现的次数，并返回counter对象"""

    # 参数类型异常检测
    try :
        if type(text) != type("") :
            raise ValueError('That was no valid list and dict')
    except ValueError :
        return 
    finally :
        print()

    # 通过jieba进行分词
    seg_list = '/'.join(jieba.cut(text, cut_all = False))

    # 通过counter进行统计英文词频
    counter_a = coll.Counter()
    list_a = []
    for i in range(len(seg_list)) :
        if seg_list[i] != '/' :
            if i == (len(seg_list)-1) : #当末尾是字母或'时，增加最后一个英文单词
                list_a.append(seg_list[i])
                counter_a["".join(list_a)] += 1
            elif (ord(seg_list[i]) not in range(65,91)) and (ord(seg_list[i]) not in range(97,123)) and (seg_list[i] != "\'") and (seg_list[i] != "_"): #将英文单词放入list和dictionary
                continue
            else :
                list_a.append(seg_list[i])
        else :
            if len(list_a) != 0 :
                counter_a["".join(list_a)] += 1
                list_a = []
    
    print('英文排序后：', counter_a.most_common(common_t), end = '\n\n')
    return counter_a.most_common(common_t)


def stats_text(text, common_t = None) :
    """分别调用stats_text_cn和stats_text_en对text中的中/英词频进行统计，按词频结果输出"""

    list_a = []
    list_b = []
    list_c = []
    j = 0

    #分别调用两个函数统计词频
    list_a = stats_text_cn(text, common_t)
    list_b = stats_text_en(text, common_t)

    for i in range(len(list_a)) :
        while j < len(list_b) :
            if list_a[i][1] < list_b[j][1] :
                list_c.append(list_b[j])
                j += 1
            else :
                break
        list_c.append(list_a[i])
    if j <= (len(list_b)) :
        while j < len(list_b) :
            list_c.append(list_b[j])
            j += 1

    print("合并排序后：", list_c,'\n')
    return list_c
