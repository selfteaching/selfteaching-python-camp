from os import path
fp = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')
file_1 = open(fp, 'rb')
file_2 = file_1.read()
file_1.closed
text = file_2.decode('utf8')
from mymodule import stats_word
result = stats_word.stats_text_cn(text)
print('词频前二十的词为：', result)