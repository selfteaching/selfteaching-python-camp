
from mymodule import stats_word as s   #从模块中导入自定义函数
from os import path                    #从os中导入路径

print(__file__, __name__)
fp =path.join(path.dirname(path.abspath(__file__)), 'tang300.json')  #找到唐诗三百首的路径
with open(fp, 'rb') as f:                                            #读取本地文件，以以 binary（二进制） mode 打开文件
    read_data =f.read()
    f.closed
    b = read_data.decode('utf8')                                     #将utf8解码为Unicode
    c3 =s.stats_text_cn(b,100) 
    print(c3.most_common(100))

try:                                 #try except  捕获异常
    print(c3.most_common(100))
except ValueError as err:
    print("err:not string ,try again")

   

    