from mymodule import stats_word
smaple_text="""
好好学习，天天向上，努力工作
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense."""

result=stats_word.stats_text(smaple_text)
print(result)