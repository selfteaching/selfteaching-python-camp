from mymodule import stats_word

sample_text = 1

result = stats_word.stats_text(sample_text)

print('统计结果 ==>',result)

try:
    result
except ValueError:
    print("error:文本为非字符串")   