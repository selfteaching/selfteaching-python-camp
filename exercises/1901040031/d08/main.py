text = 1

from mymodule import stats_word as s   #从模块中导入自定义函数

try:                                 #try except  捕获异常
    s.stats_text(text)
    print(s.stats_text(text))
except ValueError as err:
    print("err:not string ,try again")
    