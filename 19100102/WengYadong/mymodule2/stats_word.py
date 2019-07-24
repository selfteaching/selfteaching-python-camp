import re

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

#创建一个名为stats_text_en的函数，封装day5中任务2的代码到刚这个函数下，同时用文档字符串为stats_text_en添加注释说明
def stats_text_en(text):
    ''' 
    以字典形式返回字符串中英文单词的出现频率
    :param text:string
    :return dict:英文单词词频统计结果
    '''
    # 在这里写具体操作
    mydict={}
    mylist=[]
    try:
        mylist=re.findall(en_pattern,text)
    except ValueError:
        print("stats_text_en(ValueError):please input string")
    except TypeError:
        print("stats_text_en(TypeError):please input string")
    for mylinum in mylist:
        if mylinum in mydict:
            mydict[mylinum]=int(mydict[mylinum])+1
        else:
            mydict[mylinum]=1
    return mydict
#print(sorted(stats_text_en(template).items(), key=lambda d: d[1],reverse=True))

#创建一个名为stats_text_cn的函数，该函数的功能是实现统计每个中文汉字出现的次数，同时用文档字符串添加注释说明
def stats_text_cn(text):
    ''' 
    以字典形式返回字符串中文汉字的出现频率
    :param text:string
    :return dict:中文汉字词频统计结果
    '''
    # 在这里写具体操作
    mydict={}
    mylist=[]
    try:
        mylist=re.findall(cn_pattern,text)
    except ValueError:
        print("stats_text_cn(ValueError):please input string")
    except TypeError:
        print("stats_text_cn(TypeError):please input string")
    for mylinum in mylist:
        if mylinum in mydict:
            mydict[mylinum]=int(mydict[mylinum])+1
        else:
            mydict[mylinum]=1
    return mydict
#print(sorted(stats_text_cn(template).items(), key=lambda d: d[1],reverse=True))

#分别调用stats_text_en和stats_text_cn,输出合并词频统计结果
def stats_text(text):
    '''
    统计一段字符串中中文和英文的词频
    :param text:string
    :return dict:中文和英文单词词频统计结果
    '''
    dicttmp = {}
    try:
        dicttmp = dict(stats_text_en(text),**stats_text_cn(text))
    except ValueError:
        print("stats_text(ValueError):please input string")
    except TypeError:
        print("stats_text(TypeError):please input string")
    return dicttmp


def main():
    mdict={}
    mdict=stats_text(template)
    print(mdict)


if __name__ == '__main__':
    main()




