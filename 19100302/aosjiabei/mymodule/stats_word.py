
import re#导入正则表达式模块
import main
text=main.textx()#调用main.py里的textx（）函数给text赋值(为什么不把text文本字符串放在这个.py里？)
#因为我认为：被调用的stats_word.py模版封装好，不动它，text字符串文本在调用模版的main.py里输入
#如过换了文本，直接在main.py里操作

def stats_text_en():
    global text #把text标记为全局变量
    found = {}#建立空的字典
    a= text.lower()
    a=re.sub("[^\\u0061-\u007a]", " ", a)#小写字母unicode范围，筛选英文
    a=a.split()#指定分隔符对字符串进行切片
    
    for i in a:
        if i  in found:
            found[i]+=1
        else:
            found[i]=0
            found[i]+=1
    print('英文单词统计结果：',sorted(found.items(),key=lambda x:x[1],reverse=True))#词频降序
 
#统计中文词频

def stats_text_cn():
    global text #把text标记为全局变量
    found={}

    #提取中文字符串
    text= re.sub("[^\u4e00-\u9fa5]", "", text)#中文汉字unicode范围
    

    for i in text:
        if i  in found:
            found[i]+=1
        else:
            found[i]=0
            found[i]+=1

    print('中文汉字字频统计结果： ',sorted(found.items(),key=lambda x:x[1],reverse=True))


#调用stats_text_en , stats_text_cn 函数，合并统计结果

def stats_text():
    stats_text_en()
    stats_text_cn()

stats_text()

