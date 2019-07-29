from mymodule import stats_word 

path='C:/Users/Administrator/Documents/GitHub/selfteaching-python-camp/exercises/1901050042\d10/tang300.json'  
with open(path,'r',encoding='utf-8') as tan:
    tangshi= tan.read()

try : 
        a=stats_word.stats_text_cn(tangshi,20)
        print('词频最高的前20个词： ',a )
except ValueError as ve :
        print(ve)