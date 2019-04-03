# day8

#import stats_word 

#b=int(123123213213213)
#try:
   # if type(b) != str:
       # raise ValueError()
#except ValueError:
       # print("输入的不是字符串类型")
        
#a=int(input("输入字符"))
#stats_word.stats_text(a)

#day9

# 第9天作业
import mymodule.stats_word

with open('tang300.json','r',encoding='UTF-8') as f:
    text = f.read()
try:
    if not isinstance(text,str):
        raise ValueError()
    
except ValueError:
    print('输入的不是文本格式，请重新输入：')   
    
print(mymodule.stats_word.stats_text_cn(text,10))