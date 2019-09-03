# 1、加上try…except捕获异常，通过print打出方便自己调试的提示信息，让程序正常运行完毕
# 2、输出 tang300.json 文件内容中的词频前20的词和词频数

import os
import stats_word

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'tang300.json')) as f:
    read_data = f.read()
try:
    stats = stats_word.stats_text_cn(read_data,20)
except ValueError:
    print("ValueError: You have an input that is not a string.")
else:
    print(stats)