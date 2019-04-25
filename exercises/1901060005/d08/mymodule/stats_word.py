 
def judge_pure_english(keyword):
        return all(ord(c) < 128 for c in keyword)
        #判断一个字符串是否是英文字符串的函数

def stats_text_en(text):
    """1、使用字典（dict)统计text中每个英文单词出现的次数.
    2、添加类型检查，如果不是字符串类型为异常"""
    if type(text) == str:

        t1=text.replace(',',' ').replace('.','').replace('!','').replace('*',' ').replace('-','').replace('?','')#将文档中的标点符号用空格代替
        t2=t1.split()#split()就是将一个字符串分裂成多个字符串组成的列表。
        wordcount={}#定义字典
        for i in t2:  
            if judge_pure_english(i) and i != "":           
                wordcount[i]=t2.count(i)
        wordcount=sorted(wordcount.items(),key=lambda x:x[1],reverse=True)#字典参数和按值排序
        return wordcount
    else:
        if type(text) != str: #如果不是字符串类型就抛出异常
                raise ValueError ("This is not an str type")
   
text= '''Beautiful is better 中国 than ugly. Explicit is better than implicit. Simple is better than complex. Complex'''
#print(stats_text_en(text))

#清理字符串中的非中文
def is_ustr(in_str):
    out_str=''
    for i in range(len(in_str)):
        if is_uchar(in_str[i]):
            out_str=out_str+in_str[i]
        else:
            out_str=out_str+' '
    return out_str

def is_uchar(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
            return True
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar<=u'\u0039':
            return False        
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
            return False
    if uchar in ('-',',','，','。','.','>','?'):
            return False
    return False

def stats_text_cn(text):
    ''' 
    以字典形式返回字符串中文汉字的出现频率
    :param text:string
    :return dict:中文汉字词频统计结果
    '''
    if type(text) == str:
        mydict={}
        text=is_ustr(text).replace(" ","")
        for mylinum in text:
            if mylinum != "":
                if mylinum in mydict:
                    mydict[mylinum]=int(mydict[mylinum])+1
                else:
                    mydict[mylinum]=1
        mydict = sorted(mydict.items(), key=lambda d: d[1],reverse=True)
        return mydict
    else:
        if type(text) != str: #如果不是字符串类型就抛出异常
                raise ValueError ("This is not an str type")

text ="""由于每个人的心灵品质和成长环境不同，在企业 hello world 的发展过程中，多数人是在事上下功夫，少数人是在道德上下功夫，极少数人是在道上下功夫。"""
#print(stats_text_cn(text))

#分别调用stats_text_en和stats_text_cn,输出合并词频统计结果
def stats_text(text):
    '''
    统计一段字符串中中文和英文的词频
    :param text:string
    :return dict:中文和英文单词词频统计结果
    '''
    if type(text) == str:#如果text类型是字符串
    #对字符串做清洗操作，清洗掉换行、逗号，点，叹号，星号和破折号
        text=text.replace("\n"," ").replace(","," ").replace("."," ").replace("*"," ").replace("--"," ")

        return dict(stats_text_en(text)+stats_text_cn(text))
    else:
        if type(text) != str: #如果不是字符串类型就抛出异常
                raise ValueError ("This is not an str type")
text = '''面对起义，拒绝猜的诱惑.
有且只有一个办法.
Although that way may not be obvious at first unless you're Dutch.
尝试总比从未试过要强.
Although never is often better than *right* now.
如果执行很难被解释，那将是一个很糟的想法.
如果执行很容易解释，这会是一个好点子.
Namespaces are one honking great idea -- 让我们继续为之努力!'''
#print (stats_text(text))