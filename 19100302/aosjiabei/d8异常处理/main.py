from stats_word import stats_text
text=[1,2,3]
try:
    if not isinstance(text,str):#判断参数类型
        raise ValueError("非字符串参数")#抛出异常类型
    stats_text(text)
except ValueError as e:
    print("ERROR",e)
    