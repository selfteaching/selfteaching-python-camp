from stats_word import stats_text
text = ['d','b','h']
try : 
    stats_text(text)
except ValueError as ve :#捕捉错误异常并提示
    print(ve)
