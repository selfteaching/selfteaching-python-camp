from mymodule import stats_word

path = r'd:\用户目录\我的文档\GitHub\selfteaching-python-camp\exercises\1901010161\d09\mymodule\tang300.json'
with open(path, 'r', encoding='UTF-8') as f:     # byte编码的类型名称是 UTF-8

    read_date = f.read()


try:
    print('出现频率最高的前100个字： \n', stats_word.stats_text_cn(read_date, 100))
except ValueError:
    print('ValueError:type of argument is not string!')
