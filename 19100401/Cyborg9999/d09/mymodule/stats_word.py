import re
import collections

#正则表达式英文和中文字符匹配规则
en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
cn_pattern = re.compile(r'[\u4e00-\u9fa5]')

text = '''
Alice was beginning to get very bored.She and her sister were sitting under the trees.
Her sisterwas reading,but Alice had nothing to do.Once or twice she looked into her sister's book,
but ithad no pictures or conversations in it.

爱丽丝开始觉得有点无聊了。她和姐姐正坐在树下。姐姐在看书，而爱丽丝无事可做。
她不时看看姐姐的书，里面既没有图画，也没有对话。

And what is the use of a book,"thought Alice,"without pictures or conversations?
一本书没有图画和对话有什么用呢？爱丽丝想。

She tried to think of something to do,but it was a hot day and she felt very sleepy andstupid.
She was still sitting and thinking when suddenly a White Rabbit with pink eyes ran pasther.

她想找点什么事儿做做，可天气很热，她觉得又因又无聊。正坐在那儿想事，忽然，一只长着粉红眼睛的白兔跑过她身边。

There was nothing really strange about seeing a rabbit.
And Alice was not very surprised whenthe Rabbit said,Oh dear!Oh dear!I shall be late!
Perhaps it was a little strange, Alice thoughtlater,but at the time she was not surprised.

看到一只兔子真没有什么可奇怪的。兔子说话时爱丽丝居然也不觉得太奇怪。兔子说，噢，天哪！噢，天哪！我要迟到了！
后来爱丽丝想起这事觉得有点儿奇怪，但当时她并不觉得有什么奇怪。
'''

def stats_text_en(text,count):    
    
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



def stats_text_cn(text,count):
   
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