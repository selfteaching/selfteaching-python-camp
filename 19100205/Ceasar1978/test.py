import mymodule.stats_word

with open('tang300.json','r',encoding='UTF-8') as f:
    text = f.read()
    
    
print(mymodule.stats_word.stats_text_cn(text))
