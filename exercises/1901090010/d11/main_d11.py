#with open('tang300.json','r',encoding = 'UTF-8') as file:
with open('response.py','r',encoding = 'UTF-8') as file:
    a = file.read()

    from mymodule import stats_word_d11

    print(stats_word_d11.stats_text_cn(a,100)) 
 

