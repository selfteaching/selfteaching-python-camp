#encoding=utf-8
import stats_word

text = ['人生苦短，我用python']

try:
    print (stats_word.stats_text_en(text))
except ValueError:
    print('输入对象必须为字符串类型')


