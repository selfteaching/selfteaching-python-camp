import collections
import re#导入正则表达式模块

def stats_text_en(text):
    i=int (input("英文词频最高的前i个词，请输入i："))
    if not isinstance(text,str):#判断参数类型
        raise ValueError("text非字符串参数")#抛出异常类型
    a= text.lower()
    a=re.sub("[^\\u0061-\u007a]", " ", a)#小写字母unicode范围，筛选英文
    a=a.split()#指定分隔符对字符串进行切片
    print(collections.Counter(a).most_common(i))
 
#统计中文词频

def stats_text_cn(text):
    j=int (input("中文字频最高的前j个词，请输入j："))
    if not isinstance(text,str):#判断参数类型
        raise ValueError("text非字符串参数")#抛出异常类型
    #提取中文字符串
    text= re.sub("[^\u4e00-\u9fa5]", "", text)#中文汉字unicode范围
    print(collections.Counter(text).most_common(j))


#调用stats_text_en , stats_text_cn 函数，合并统计结果

def stats_text(text):
    stats_text_en(text)
    stats_text_cn(text)




