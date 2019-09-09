from mymodule import stats_word

with open('/Users/jiamiaomiao/Documents/GitHub/selfteaching-python-camp/exercises/1901100296/d09/tang300.json') as f:
    text=f.read()
f.close()
try:
    # print('统计结果：',stats_word.stats_text(text2))
    # print('统计结果：',stats_word.stats_text_en(text))
    print('统计结果：',stats_word.stats_text_cn(text,100))
except ValueError as err:
    print('发现错误：',err)

