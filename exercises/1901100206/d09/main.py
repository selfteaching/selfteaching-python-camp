import json
from  mymodule import stats_word
path = r'D:\Github文件\selfteaching-python-camp\exercises\1901100206\d09\tang300.json' #读取本地路径
try:
    #先转换成unicode，否则'gbk' codec can't decode byte 0x80 in position 70: illegal multibyte sequence
    with open(path, "r", encoding='UTF-8') as f:  #"r"可不加
        read_one = f.read() #read()将文件内容读取，并存在read_one
        print(stats_word.stats_text_cn(read_one, 100)) 
except TypeError as err:
    print('TypeError:' + str(err))


