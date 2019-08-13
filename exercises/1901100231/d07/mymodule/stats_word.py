import re#运用正则表达式来去除符号和非目标文字
def stats_text_en(x) :#定义英文单词词频统计函数
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
  b = sorted(a.items(),key=lambda x:x[1],reverse=True)#对合并字典排序得到合并词频统计结果
  return(b)#返回值用于合并统计结果
def stats_text_cn(x) :#定义汉字字频统计函数
   x = re.sub(u"[^\u4e00-\u9fa5]"," ",x)#去除英文和其他非中文的特殊符号
   x = x . replace("\n"," ")#去除换行符
   x = x . replace(""," ")#由于汉字输入字和字之间无间隔会导致所有汉字文本共同算作列表中的一个元素，所以人为添加空格将汉字分隔开以便于统计。其余的套用英文文本处理的程序
   copy = x.split(' ')#将文本转换为列表
   copy = [i for i in copy if i != ""]#去除之前人为添加的空格，避免影响统计结果
   a = {}#创建新字典
   for i in copy :#对copy中汉字进行字频统计，此前已有的key的value值加一，此前未有的key的value为1
    if i in a:
      a[i] = a[i]+1
    else:
      a[i] = 1
   b = sorted(a.items(),key=lambda x:x[1],reverse=True)#对合并字典排序得到合并词频统计结果
   return(b)#返回值用于合并统计结果
def stats_text(x) :#定义混合词频统计函数
  stats_text_en(x)
  stats_text_cn(x)#引用两函数分别得到两个词频统计结果
  a = stats_text_cn(x)+stats_text_en(x)#合并两词频统计结果
  print(a)#输出合并词频统计结果