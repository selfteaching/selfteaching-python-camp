from mymodule import stats_word  
import json   # 读取本地文件模块


# string = 123456789
# try:
#     stats_word.stats_text(string)
# except ValueError as error:
#     print(error)


#读取本地文件，进行词频统计

with open(r'E:\xuefeng\selfteaching-python-camp\exercises\1901100277\Day 09\mymodule\tang300.json', 'r',encoding='utf-8') as f:
    #  https://www.liaoxuefeng.com/wiki/1016959663602400/1017607179232640  廖雪峰:文件的读写

    cn_text = f.read()  # 读取文件全部内容,如果文件比较大,会浪费很多系统资源,更优的选择是 读取部分文件.模块有介绍
    

print(stats_word.stats_text_cn(cn_text))




