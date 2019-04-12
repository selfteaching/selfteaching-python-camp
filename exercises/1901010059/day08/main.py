

a = ('happy','happy','happy','哈哈哈')

from mymodule.stats_word import stats_text_cn as cn
try:                #添加一个try except 捕获异常
    cn(a)
except ValueError as Type_Error:
    print(Type_Error)
print(cn(a)) 
#任选一个函数用a测试参数类型检测是否成功
