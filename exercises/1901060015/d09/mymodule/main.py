import json
with open('tang300.json',mode='r+',encoding='utf-8') as text:
    text=text.read()
    
import stats_word
try:
    
    print(stats_word.stats_text_cn(text))
    
except:
    print("omg! please try again!!!")


        
        
       
    

   