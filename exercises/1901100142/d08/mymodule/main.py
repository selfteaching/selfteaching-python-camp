import stats_word
text = 12
try:
    stats_word.stats_text_cn(text)
except ValueError:
    print('Error:文本为非字符串')