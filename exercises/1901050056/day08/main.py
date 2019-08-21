from mymodule import stats_word

text = 'aaa,aaa,aaa,sdafasdf,sadfasdf,asdfsadf,你好,你好,你好,世界'
text = []
try:
    stats_word.stats_text(text)
except  ValueError as va:
    print(va)