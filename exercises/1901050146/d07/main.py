from mymodule import stats_word

sample_text='''
愚公移山
太行，王屋二山的北面，住了一个九十岁的老翁，名叫愚公。

How the Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high mountains,
Mountains, Mount Taixing and Mount Wangwu.
'''

result=stats_word.stats_text(sample_text)
print('统计结果',result)