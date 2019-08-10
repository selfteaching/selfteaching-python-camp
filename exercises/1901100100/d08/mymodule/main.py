# -*- coding: GBK -*-
import stats_word
import traceback
text = 2.598
#text = stats_word.text
try:
    dict_order = stats_word.stats_text(1)
except ValueError as e:
    print("the text needed to be sorted is not a string, please try again!\n ",e)
    #this sentence is use to print the information of the exception
    print(traceback.format_exc())
