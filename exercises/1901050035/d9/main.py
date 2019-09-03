#Selfteaching day9 homework ,updating  main.py program!

from mymodule import stats_word as counts  #import module stats_word.py function
   
text = 1314520  # 用 try...except 触发异常并执行
try:
    counts.stats_text(text,10)
except ValueError:
    print("Input was not string. Try again...")

text ='''  '''
import json
with open('tang300.json',encoding='utf-8') as f:
     lines=f.readlines()
f.close()   
text=str(lines).strip()

print('唐诗最多的100字:',counts.stats_text_cn(text,100)) #output all the chines words counts before 100
