#作者：邓超
#作业：封装’按照字母降序统计英文词频‘的函数
def stats_text_en(text):    #定义一个函数
    text = text.replace('.', '').replace(',','').replace('*','').replace('-','')
    text = text.split()   #转换成列表                                      #去除标点符号
    import collections 
    m=collections.Counter(text)         #遍历排序
    return (m)

#示例：
a = '''Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
print(stats_text_en(a))
    #  stats_text_en  函数作用：按照降序统计单词出现的次数，并去除符号。
                     #函数用法： stats_text_en(a)

#封装“统计中文词频出现次数，并按照降序输出。、
def stats_text_cn(text):    #定义一个函数
    text = text.replace('!','').replace('。','').replace('，','').replace(':','')
    text_list = text.split()     #转换成列表                       #去除一些符号
    import collections
    m = collections.Counter(text)     #排序  
    return(m)

#示例：
a = '''这个函数的作用是：统计中文词频，并按照降序数组排列，同时去除符号，这些符号包括！和，和。和'''
print(stats_text_cn(a))

        #该函数可以统计中文出现的频次，并按照降序排列
stats_text = (stats_text_en+stats_text_cn)

a = '''Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
这个函数的作用是：统计中文词频，并按照降序数组排列，同时去除符号，这些符号包括！和，和。和'''

print(stats_text)




