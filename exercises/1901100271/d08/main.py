from mymodule import stats_word
text = 1,2,3
try:
    stats_word.stats_text(text)
except ValueError:
    print("错误：文本为非字符串格式")

