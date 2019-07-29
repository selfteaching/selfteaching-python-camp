#引用function 
import Stats_word

#引用tang.300文件并读取
with open('tang300.json') as t:
    text = t.read()
t.closed

#Day8内容，尝试引用
try:
    print('前20的中文词频统计结果： ', Stats_word.stats_text_cn(text)) #没有英文，直接调用的中文统计
except:
    print("对象不是字符串类型！")

