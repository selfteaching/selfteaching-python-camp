


from mymodule import stats_word
s = 369
try:
    stats_word.stats_text_en(s)
except ValueError:
    print('Error:文本为非字符串,请输入字符串')



