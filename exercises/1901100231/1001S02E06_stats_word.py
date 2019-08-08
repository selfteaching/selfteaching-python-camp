#本程序仅能统计纯英文文本或纯汉字文本
def stats_text_en(x) :#定义英文单词词频统计函数
  x = x.lower()#统一大小写以便排序
  for y in '!"#$&()*+,-./:;<=>?@[\\]^_{|}·~‘’':#去除标点符号
    x = x .replace(y," ")
  x = x . replace("\n"," ")#去除换行符
  copy = x.split(' ')#将文本转换为列表
  copy = [i for i in copy if i != ""]#去除空格，避免影响统计结果
  a = {}#创建新字典
  for i in copy :#对copy中单词进行词频统计，此前已有的key的value值加一，此前未有的key的value为1
    if i in a:
      a[i] = a[i]+1
    else:
      a[i] = 1
  b = sorted(a.items(),key=lambda x:x[1],reverse = True)#对字典a按照值反向排序并将排序结果形成一个列表
  print(b)
def stats_text_cn(x) :#定义汉字字频统计函数
   for y in '!"#$&()*+,-./:;<=>?@[\\]^_{|}·~‘’，。！？、':#去除标点符号（相对于英文处理的程序添加了中文符号）
     x = x .replace(y," ")
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
   b = sorted(a.items(),key=lambda x:x[1],reverse = True)#对字典a按照值反向排序并将排序结果形成一个列表
   print(b)
function = input("英文统计输入1，汉字统计键入2：")
print("请输入要统计的文本(输入结束时请按space+enter):")
stop = " "#将终止符号改为空格，防止文本中空白行终止输入的情况发生
text = ""#此处必须提前定义好用于存放用户输入文字的字符串text
for x in iter(input,stop):#遍历用户输入的input中的每个字符并将其添加至text字符串中，直到遇到终止命令stop，避免换行时输入的“\n”导致的输入终止，使程序可以接收多行文字信息。
    text += x +"\n"  #不知道原因，换行符会被忽略，导致一行末尾的单词会和下一行行首的单词相连。猜测+"\n"的作用为使文本中的换行符不被忽略？
print (text)
if function =="1":
      stats_text_en(text)
elif function =="2":
      stats_text_cn(text)
