import stats_word
text = 369
try:
    stats_word.stats_text_en(text)
except ValueError:
    print('Error:文本为非字符串')