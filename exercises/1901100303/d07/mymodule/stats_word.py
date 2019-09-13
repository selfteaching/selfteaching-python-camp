def stats_text_en(text):        #定义函数
    #统计参数中每个英⽂文单词出现的次数，最后返回⼀一个按词频降序排列列的数组
    text_list = text.split()  #字符串切片，赋值给list
    counter = {}             #定义字典
    return_list = {}         #定义返回值
    text_set =set(text_list)    #list去重
    for i in text_set:           #
        counter[i] = text_list.count(i)
    
    return_list = sorted(counter.items(),key=lambda x:x[1],reverse = True)
    return return_list


def stats_text_cn(text_cn):
    #统计参数中每个中文汉字出现的次数，最后返回⼀一个按字频降序排列列的数组
    cn_char= []
    for char in text_cn:
        cn_char.append(char)

    counter_cn = {}
    return_list_cn = {}
    text_set_cn = set(cn_char)
    
    for j in text_set_cn:
        counter_cn[j] = cn_char.count(j)
    
    return_list_cn = sorted(counter_cn.items(),key=lambda x:x[1],reverse= True)
    
    return return_list_cn
    
#print(stats_text_cn("""中国共产党万岁，中国人民万岁"""))

def stats_text():
    #调用stats_text_en 和 stats_text_cn 两个函数，将两个函数的输出结果合并为一个list，输出。
    main_list = []
    main_list = stats_text_en("""The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.""") + stats_text_cn("""中国共产党万岁，中国人民万岁""")
    
    return main_list 
print(stats_text())    