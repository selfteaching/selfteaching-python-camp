from mymodule import stats_word 

test1 = 3.1415926  # 用 try except 捕获异常并执行
try:
    stats_word.stats_text(test1)
except ValueError:
    print("大哥，要输入文本啊")
except TypeError:
    print("大姐，要输入文本啊，你输错啦")

text = '''
愚公移山
@@ -49,3 +56,8 @@
'''

stats_word.stats_text(text)

#sw.stats_text_cn(1) #测试触发异常
#sw.stats_text_en(1) #测试触发异常
#sw.stats_text(1)    #测试触发异常