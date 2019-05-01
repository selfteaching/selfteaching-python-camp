import stats_word
text = (1,2,3,4)
try:
    stats_word.stats_text(text)
    pass
except ValueError:
    print('不是字符串，请重新输入')
