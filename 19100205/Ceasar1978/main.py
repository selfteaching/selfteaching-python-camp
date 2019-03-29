# 第8天作业
import mymodule.stats_word
text = input("请输入要统计词频的文本：")
try:
    if not isinstance(text,str):
        raise ValueError()
    
except ValueError:
    print('输入的不是文本格式，请重新输入：')
print(mymodule.stats_word.stats_text(text))

# 第9天作业
import mymodule.stats_word

with open('tang300.json','r',encoding='UTF-8') as f:
    text = f.read()
try:
    if not isinstance(text,str):
        raise ValueError()
    
except ValueError:
    print('输入的不是文本格式，请重新输入：')   
    
print(mymodule.stats_word.stats_text_cn(text))