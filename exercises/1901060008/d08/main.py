from mymodule import stats_word
a=(1,99,199,9999)
s = {'梁峰':88,'韦彩兰':88}
t=[55,88,99]
b='1855555222214862'

stats_word.stats_text_en(a)
stats_word.stats_text_cn(s)
stats_word.stats_text(t)
stats_word.stats_text_en(a)
try:
    stats_word.stats_text_en(b)
 
except IndexError:
    print('list index out of range, Enter a short array')

