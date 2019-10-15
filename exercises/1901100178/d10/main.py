import json, os
from  mymodule import stats_word
#path = r'D:\My Documents\Programming Days\selfteaching-python-camp\exercises\1901100178\d09\tang300.json' #读取本地路径
#path = os.path.abspath(__file__) 显示当前文件，即main.py的绝对路径
#path = os.path.dirname(os.path.abspath(__file__)) 显示main.py所在文件夹的目录
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json') #实现效果与第一个path相同
try:
    #先转换成unicode，否则'gbk' codec can't decode byte 0x80 in position 70: illegal multibyte sequence
    with open(path, "r", encoding='UTF-8') as f:  #"r"可不加
        read_one = f.read() #read()将文件内容读取，并存在read_one
        print(stats_word.stats_text_cn(read_one, 100)) 
except TypeError as err:
    print('TypeError:' + str(err))