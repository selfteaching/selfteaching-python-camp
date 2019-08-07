#本程序只可用于纯英文文本，成段的汉字文本会被视为一个元素进行统计，故不能用于汉字字频统计
print("请输入要统计词频的英文文本(输入完成时请双击回车键“Enter”):")
stop = ""#设定终止符号为空白行
text = ""#此处必须提前定义好用于存放用户输入文字的字符串text
for x in iter(input,stop):#遍历用户输入的input中的每个字符并将其添加至text字符串中，直到遇到终止命令stop，避免换行时输入的“\n”导致的输入终止，使程序可以接收多行文字信息。
    text += x +"\n"  #不知道原因，换行符会被忽略，导致一行末尾的单词会和下一行行首的单词相连。猜测+"\n"的作用为使文本中的换行符不被忽略？
print (text)
def stats_text_en(x) :#定义文字处理函数
   x = x.lower()#统一大小写以便排序
   for y in '!"#$&()*+,-./:;<=>?@[\\]^_{|}·~‘’':#去除标点符号
     x = x .replace(y,"")
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
stats_text_en(text)#将用户输入的text作为参数代入已定义好的函数中使用
