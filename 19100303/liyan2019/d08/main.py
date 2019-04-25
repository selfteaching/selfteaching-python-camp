from mymodule import stats_word as sw 
# 后面没有冒号
# from stats_word.py import stats_text  【注意这种错误和前述正确的区别】
# 调用 stats_text(text),参数传入非字符串，验证参数检查功能是否生效。
# 加上try...except 捕获异常，并print出方便自己调试的信息。
text=[1,2,3,4]
try:
    sw.stats_text(text)
    print(sw)

except ValueError:
    print('Not string. Try again...')

