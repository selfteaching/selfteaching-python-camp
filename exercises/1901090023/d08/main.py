# 调用stats_word中的第三个函数
from mymodule.stats_word import stats_text     # 从 模块中 导入 函数
text = 'hello world! 你好啊，世界!'

try:
    print(stats_text(text))                    # 假设调用者忘了输入text，由于text没有被定义，则由except来捕获NameError异常
except NameError as err:
    print('Oops, cannot find text! Please input text!')
else:                                          # 如果调用者正确定义了text,即无错误发生，则执行else语句
    print('no error')
finally:                                       # 不管有无异常，最后都要执行finally语句，让程序按流程执行完。
    print('The end')


