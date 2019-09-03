import re
import collections

#英文和中文字符匹配规则
en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
cn_pattern = re.compile(r'[\u4e00-\u9fa5]')

text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to 打破规则.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

           

#创建一个名为stats_text_en的函数,封装day5中的代码到这个函数下，同时添加注释说明
def stats_text_en(text,count):    
    #以字典形式返回字符串中英文单词的出现频率
    #:param text:string
    #:return dict:英文单词排序结果
    
    #以下是具体操作
    mydict = []
    mylist = []
    try:
        mylist=re.findall(en_pattern,text)
    except ValueError:
        print("stats_text_en(ValueError):please input string")
    except TypeError:
        print("stats_text_en(TypeError):please input string")
    # 实现英文单词词频统计的模块(old)
    # for mylinum in mylist:
    #      if mylinum in mydict:
    #          mydict[mylinum]=int(mydict[mylinmu])+1
    #      else:
    #          mydict[mylinum]=1
    #实现英文单词词频统计的模块（new），用python自带的Counter函数
    mydict=collections.Counter(mylist).most_common(count)
    return mydict
#print(sorted(stats_text_en(text).items(),key=lambda d:d[1],reverse=True))


#创建一个名为stats_text_cn的函数，实现统计每个中文汉字出现的次数，同时添加注释说明
def stats_text_cn(text,count):
    #以字典形式返回字符串中文汉字的出现频率
    #:param text:string 输入的字符串
    #:param count:int 控制输出个数
    #:return list:中文汉字词频统计结果（列表形式输出)

    #以下是具体操作
    mydict=[]
    mylist=[]
    try:
        mylist=re.findall(cn_pattern,text)
    except ValueError:
        print("stats_text_cn(ValueError):please input string")
    except TypeError:
        print("stats_text_cn(TypeError):please input string")
    mydict=collections.Counter(mylist).most_common(count)
    return mydict

#创建一个名为stats_text的函数，实现统计字符串中英文单词和中文汉字的词频
def stats_text(text,rmodel,count):
    #统计一段字符串中中文和英文的词频
    #:param text:string 输入的字符串
    #:param rmode:int 读取类型 1:中文 2:英文 0:中英混合
    #:param count:int 控制输出个数
    #:return list:中文和英文单词词频统计结果（列表形式输出）
    mylist_en=[]
    mylist_en=re.findall(en_pattern,text)
    mylist_cn=[]
    mylist_cn=re.findall(cn_pattern,text)
    dicttmp = []
    try:
        if rmodel==1:
            dicttmp=collections.Counter(mylist_cn).most_common(count)
        elif rmodel==2:
            dicttmp=collections.Counter(mylist_en).most_common(count)
        else:
            dicttmp=collections.Counter(mylist_en+mylist_cn).most_common(count)
    except ValueError:
        print("stats_text(ValueError):please input string")
    except TypeError:
        print("stats_text(TypeError):please input string")
    return dicttmp

def main():
    mdict=[]
    mdict=stats_text(text,1,30)
    print(mdict)

if __name__=='__main__':
    main()