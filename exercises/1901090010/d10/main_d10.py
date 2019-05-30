with open('tang300.json','r',encoding = 'UTF-8') as file:
    a = file.read()

    from mymodule import stats_word_d10

    print(stats_word_d10.stats_text_cn(a,20)) 
 