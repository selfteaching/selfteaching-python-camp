from mymodule import stats_word as sw 
# 后面没有冒号
# from stats_word.py import stats_text  【注意这种错误和前述正确的区别】
text='''
中文中国. I love China and China.'''
sw.stats_text(text)
#为什么不是：sw(text)
print(sw)