from mymodule import stats_word

string = 123456789
try:
    stats_word.stats_text(string)
except ValueError as error:
    print(error)

AAA = stats_word.stats_text(string)
print("统计 英文单词字频 和中文字频 的结果,并按从大到小排列：",AAA)



