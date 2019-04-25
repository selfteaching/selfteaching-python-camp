from mymodule import stats_word as chkt

text = [1,2,3,'许哦我']
try:
    chkt.stats_text(text)
except ValueError as err:
     print(err)
