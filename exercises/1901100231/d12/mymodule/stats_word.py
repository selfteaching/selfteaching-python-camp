import re#运用正则表达式来去除符号和非目标文字
import collections#运用collections模块进行词频统计
import jieba
def exam(x):#定义参数类型检查函数，若非字符串类型则抛出ValueError类型错误并提示错误类型
    if not isinstance(x,str): 
      raise ValueError("您输入的不是字符，请重新尝试，输入字符类型的参数。")
    else:
      pass
def stats_text_en(x,count) :#定义英文单词词频统计函数
    exam (x)#检查参数类型正确与否
    count = int(count)#设定int类型变量count以限制输出元素个数
    x = x.lower()#统一大小写以便排序
    x = re.sub(u"[^\u0061-\u007a’']"," ",x)#去除非英文和’'符号的其他文本，防止影响英文词频的统计
    x = x . replace("\n"," ")#去除换行符
    copy = x.split(' ')#将文本转换为列表
    copy = [i for i in copy if i != ""]#去除空格，避免影响统计结果
    a = {}#创建新字典
    for i in copy :#对copy中单词进行词频统计，此前已有的key的value值加一，此前未有的key的value为1
      if i in a:
        a[i] = a[i]+1
      else:
        a[i] = 1
    b = collections.Counter (a).most_common(count)#对字典排序得到词频统计结果
    return(b)#返回值用于合并统计结果
def stats_text_cn(x,count) :#定义汉字字频统计函数
    exam (x)#检查参数类型正确与否
    count = int(count)#设定int类型变量count以限制输出元素个数
    x = re.sub(u"[^\u4e00-\u9fa5]"," ",x)#去除英文和其他非中文的特殊符号
    x = x . replace("\n"," ")#去除换行符
    x = jieba.lcut(x,cut_all = False)#利用结巴分词
    copy = [i for i in x if len(i)>1]#去除文本中的单字和空格
    a = {}#创建新字典
    for i in copy :#对copy中汉字进行字频统计，此前已有的key的value值加一，此前未有的key的value为1
      if i in a:
        a[i] = a[i]+1
      else:
        a[i] = 1
    b = collections.Counter (a).most_common(count)#对字典排序得到词频统计结果
    return(b)#返回值用于合并统计结果
def stats_text(x,count) :#定义混合词频统计函数（引用的函数中已有参数类型检查步骤，故不再添加参数类型检查步骤）
    a = stats_text_cn(x,count)+stats_text_en(x,count)#合并两词频统计结果
    return(a)#返回统计值
