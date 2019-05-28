from  stats_word_d9 import stats_text_cn

#把tang.json转换成UTF-8字符串格式
with open('tang300.json','r',encoding='UTF-8') as f:
    text = f.read()
    try:
        stats_text_cn(text)
    except ValueError as e:
        print("ERROR",e)




