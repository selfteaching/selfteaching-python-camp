

a = ('One','Two','Three','一二三')

from mymodule.stats_word import stats_text_cn as cn
try:                #添加一個try except 捕獲異常
    cn(a)
except ValueError as Type_Error:
    print(Type_Error)
print(cn(a)) 
#任選一個函數用a測試參數類型檢測是否成功
