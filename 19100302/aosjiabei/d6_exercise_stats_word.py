text='''It is the time you have wasted for your rose that makes your rose so important
你在你的玫瑰花身上耗费的时间,使得你的玫瑰花变得如此重要!!!!!!!!!!!!!'''


a= text.lower()
a=a.split()#指定分隔符对字符串进行切片
a.pop()#删除list中的中文元素
found = {}#建立空的字典
def stats_text_en():
    global text #把text标记为全局变量
    for i in a:
        if i  in found:
            found[i]+=1
        else:
            found[i]=0
        found[i]+=1
    print('英文单词统计结果：',sorted(found.items(),key=lambda x:x[1],reverse=True))#词频降序

    
stats_text_en()




#统计中文词频


import re

def stats_text_cn():
    global text #把text标记为全局变量
    found={}

    #提取中文字符串
    text= re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", text)
    text=text.replace( "  ",'')#提取的中文字符串会算上空格，会被统计上，故移除空格
    print(text)

    for i in text:
        if i  in found:
            found[i]+=1
        else:
            found[i]=0
            found[i]+=1

    print('中文汉字字频统计结果： ',sorted(found.items(),key=lambda x:x[1],reverse=True))

stats_text_cn()


   