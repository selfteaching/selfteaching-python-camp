from mymodule import state_word
text=[1,2,3,4]
try:
     result = state_word.stats_text(text)
except ValueError:
     print("输入的不是字符串类型") 
