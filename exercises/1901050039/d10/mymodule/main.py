#调用模块
import stats_word

#输入测试文本
with open('/Users/AbbyHuang/Documents/GitHub/selfteaching-python-camp/exercises/1901050039/d09/mymodule/tang300.json','r') as f:
    text = f.read()

#参数类型检查
try:
    a = stats_word.stats_text_cn(text)
    print(a)
except ValueError:
    print('Error:参数格式不对，请更换为文本')