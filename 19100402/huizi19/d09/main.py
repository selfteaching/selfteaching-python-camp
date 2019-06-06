from mymodule import stats_word 
path='C:/Users/lenovo/Documents/GitHub/Day/selfteaching-python-camp/19100402/huizi19/d09/tang300.json'
with open(path,'r',encoding='utf-8') as tan:
    text= tan.read()



try : 
        print('词频最高的前100个词： ', stats_word.stats_text_cn(text,100))
except ValueError as ve :
        print(ve)