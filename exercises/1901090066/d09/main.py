from mymodule import state_word
fo=open("//Users//zhangyuxiaowanzi//Documents//English//selfteaching-python-camp//exercises/1901090066//d09//tang300.json","r")
text=fo.read()
fo.close
try:
    print('统计字数最多的前100个字：',state_word.stats_text_cn(text,100))
except ValueError :
    print('输入异常') 
