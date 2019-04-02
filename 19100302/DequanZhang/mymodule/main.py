from stats_word import stats_text_cn   #调用函数

with open('tang300.json','r',encoding='UTF-8') as f:
    text = f.read()

    try:
        print("词频Top100:" stats_text_cn(text,100))
    except ValueError as Error:
        print('仅接受字符串类型参数，输入的不是字符串，请重新输入：')  


