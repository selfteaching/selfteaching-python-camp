from mymodule.stats_word import stats_text_en
from mymodule.stats_word import stats_text_cn
from mymodule.stats_word import stats_txt
text=[1,2,3,4,5]
dic_test={}
try:
    dic_test=stats_text_en(text)
except ValueError:
    print("Could only deai with string,check input and try again.")