from  stats_word import stats_text
text=123
try:
    print(stats_text(text))
except ValueError:
    print('请重新输入字符串内容！')