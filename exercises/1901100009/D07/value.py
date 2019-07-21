from mymodule import stats_word

sample_text = '''

这个自己做的字数统计测试就是不出结果，不知道是字数原因还是程序哪里出了问题。

'''
result = stats_word.stats_text(sample_text)
print = ('统计结果==>',result)