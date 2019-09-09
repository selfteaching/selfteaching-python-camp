from mymodule10 import stats_word10

path = r'd:\用户目录\我的文档\GitHub\selfteaching-python-camp\exercises\1901010161\d10\mymodule10\tang300.json'
with open(path, 'r', encoding='UTF-8') as f:     # byte编码的类型名称是 UTF-8

    read_date = f.read()


try:
    print('出现频率最高的前20个词： \n', stats_word10.stats_text_cn(read_date, 20))
except ValueError:
    print('ValueError:type of argument is not string!')
