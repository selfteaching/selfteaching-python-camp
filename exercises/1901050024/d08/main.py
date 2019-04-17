from mymodule import stats_word

test = (12312,123123) #用于 try except 捕获异常并执行

try:
    stats_word.stats_text_en(test)
except ValueError as a:
    print(a)


try:
    stats_word.stats_text_cn(test)
except ValueError as a:
    print(a)


try:
    stats_word.stats_text(test)
except ValueError as a:
    print(a)