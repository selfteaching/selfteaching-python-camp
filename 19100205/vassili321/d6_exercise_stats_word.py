# 此文件用函数封装统计词频及排序的操作

def stats_text_en(text) :
    """统计text中每个英文单词出现的次数，并返回一个按词频降序排列的数组"""
    list_a = []
    j = 0
    # 将字符串放入list容器中
    for i in range(len(text)) :
        if (ord(text[i]) not in range(65,91)) and (ord(text[i]) not in range(97,123)) and (text[i] != "\'") :
            if i == j :
                j += 1
            else :
                list_a.append(text[j:i])
                j = i + 1
        elif i == (len(text)-1) : #当末尾是字母或'时，增加最后一个单词
            list_a.append(text[j:i])
    if len(list_a) == 0 :
        return
    print('list：', list_a, end = '\n\n')
    
    # 通过dictionaries 进行统计词频并按照降序输出
    dic_b = {}
    for i in range(len(list_a)) :
        if list_a[i] not in dic_b :
            dic_b[list_a[i]] = 1
        else :
            dic_b[list_a[i]] += 1
    print('dictionaries：', sorted(dic_b.items(), key = lambda x:x[1], reverse = True), end = '\n\n')
    
    # 返回排序后的数组
    list_b = []
    list_c = []
    list_b = list(sorted(dic_b.items(), key = lambda x:x[1], reverse = True))
    for i in range(len(list_b)) :
        list_c.append(list_b[i][0])
    return list_c



def stats_text_cn(text) :
    """统计text中每个中文单词出现的次数，并返回一个按词频降序排列的数组"""
    list_a = []
    # 将字符串放入list容器中
    for i in range(len(text)) :
        if (text[i] >= '\u4e00') and (text[i] <= '\u9fa5') :
            list_a.append(text[i])
    if len(list_a) == 0 :
        return
    print('列表：', list_a, end = '\n\n')
    
    # 通过dictionaries 进行统计词频并按照降序输出
    dic_b = {}
    for i in range(len(list_a)) :
        if list_a[i] not in dic_b :
            dic_b[list_a[i]] = 1
        else :
            dic_b[list_a[i]] += 1
    print('字典：', sorted(dic_b.items(), key = lambda x:x[1], reverse = True), end = '\n\n')
    
    # 返回排序后的数组
    list_b = []
    list_c = []
    list_b = list(sorted(dic_b.items(), key = lambda x:x[1], reverse = True))
    for i in range(len(list_b)) :
        list_c.append(list_b[i][0])
    return list_c



list_d = []
int_a = 1
while int_a != 0 :
    string_a = input('请选择输入的语言[English / 中文] :') #选择控制结构
    if string_a == 'English' :
        string_b = input('\n' 'Please enter content :' '\n')
        list_d = stats_text_en(string_b) # stats_text_en()函数调用
        if list_d == None :
            print('No English input' '\n')
        else :
            print('The end list of sorted :',list_d)
            int_a = 0
    elif string_a == '中文' :
        string_b = input('\n' '请输入内容 :' '\n')
        list_d = stats_text_cn(string_b) # stats_text_cn()函数调用
        if list_d == None :
            print('无中文输入' '\n')
        else :
            print('最终排序列表 :',list_d)
            int_a = 0
    else :
        print('输入错误，请重新输入' '\n')