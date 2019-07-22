import stats_word
text = 89  #一个非字符串
try: #执行正常的代码
    text_list= stats_word.stats_text_en(text)
    print(text_list)
except ValueError as identifier: #如果检测到ValueError打印出来
    print('请输入字符串',identifier) 
