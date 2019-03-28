import re
import collections
import jieba

#英文和中文字符匹配规则
en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
cn_pattern = re.compile(r'[\u4e00-\u9fa5]')

#字符串示例
template = '''
The Zen of Python, by Tim Peters
美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
可读性计数.
Special cases aren't special enough to 打破规则.
即使练习会使得不再纯粹.
但错误不应该用沉默来掩盖.
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
有且只有一个办法.
Although that way may not be obvious at first unless you're Dutch.
尝试总比从未试过要强.
Although never is often better than *right* now.
如果执行很难被解释，那将是一个很糟的想法.
如果执行很容易解释，这会是一个好点子.
Namespaces are one honking great idea -- 让我们继续为之努力!
'''

#检验是否全是中文字符
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

#创建一个名为stats_text_en的函数，封装day5中任务2的代码到刚这个函数下，同时用文档字符串为stats_text_en添加注释说明
def stats_text_en(text,count=None):
    ''' 
    以字典形式返回字符串中英文单词的出现频率
    :param text:string 输入的字符串
    :param count:int 控制输出个数
    :return list:英文单词词频统计结果(列表形式输出)
    '''
    # 在这里写具体操作
    mydict=[]
    mylist=[]
    try:
        mylist=re.findall(en_pattern,text)
    except ValueError:
        print("stats_text_en(ValueError):please input string")
    except TypeError:
        print("stats_text_en(TypeError):please input string")
    # #实现英文单词词频统计的模块（old）
    # for mylinum in mylist:
    #     if mylinum in mydict:
    #         mydict[mylinum]=int(mydict[mylinum])+1
    #     else:
    #         mydict[mylinum]=1
    #实现英文单词词频统计的模块（new），用python自带的Counter函数
    mydict=collections.Counter(mylist).most_common(count)

    return mydict
#print(sorted(stats_text_en(template).items(), key=lambda d: d[1],reverse=True))

#创建一个名为stats_text_cn的函数，该函数的功能是实现统计每个中文汉字出现的次数，同时用文档字符串添加注释说明
def stats_text_cn(text,count=None):
    ''' 
    以字典形式返回字符串中文汉字的出现频率
    :param text:string 输入的字符串
    :param count:int 控制输出个数
    :return list:中文汉字词频统计结果（列表形式输出）
    '''
    # 在这里写具体操作
    mydict=[]
    mylist=[]
    mylisttemp=[]
    try:
        #mylist=re.findall(cn_pattern,text)
        mylist=jieba.lcut(text,cut_all=False)
        for mylistitem in mylist:
            if is_all_chinese(mylistitem)==True and len(mylistitem)>=2:
                mylisttemp.append(mylistitem)

    except ValueError:
        print("stats_text_cn(ValueError):please input string")
    except TypeError:
        print("stats_text_cn(TypeError):please input string")
    # #实现英文单词词频统计的模块（old）
    # for mylinum in mylist:
    #     if mylinum in mydict:
    #         mydict[mylinum]=int(mydict[mylinum])+1
    #     else:
    #         mydict[mylinum]=1
    #实现英文单词词频统计的模块（new），用python自带的Counter函数
    mydict=collections.Counter(mylisttemp).most_common(count)

    return mydict
#print(sorted(stats_text_cn(template).items(), key=lambda d: d[1],reverse=True))

#创建一个名为stats_text的函数，该函数的功能是实现统计字符串中英文单词和中文汉字的词频
def stats_text(text,rmodel,count=None):
    '''
    统计一段字符串中中文和英文的词频
    :param text:string 输入的字符串
    :param rmode:int 读取类型 1:中文 2:英文 0:中英混合
    :param count:int 控制输出个数
    :return list:中文和英文单词词频统计结果（列表形式输出）
    '''
    mylist_en=[]
    mylist_en=re.findall(en_pattern,text)
    mylist_cn=[]
    mylist_cn=re.findall(cn_pattern,text)
    dicttmp=[]
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
    mdict=stats_text_cn(template,10)
    print(mdict)


if __name__ == '__main__':
    main()