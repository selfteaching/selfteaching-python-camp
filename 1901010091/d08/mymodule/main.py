import stats_word
test=123456
try:
    stats_word.stats_text(test)
except ValueError:
    print("文本为非字符串")

