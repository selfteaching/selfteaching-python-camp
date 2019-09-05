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
print(stats_text_en("""The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense."""))
