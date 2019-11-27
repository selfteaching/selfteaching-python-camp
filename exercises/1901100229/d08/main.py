text = [2,3,4,5]
 
from mymodule.stats_word import stats_text_cn as cn 
try:            #添加一个try except捕获一次
    cn(text)
except ValueError as Type_Error:
    print(Type_Error)
print(cn(a))












