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

#判断一个字符串是否是英文字符串的函数
def judge_pure_english(keyword):
        return all(ord(c) < 128 for c in keyword)

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


#对字符串做清洗操作，清洗掉换行、逗号，点，叹号，星号和破折号
template=template.replace("\n"," ").replace(","," ").replace("."," ").replace("*"," ").replace("--"," ")

#创建一个名为stats_text_en的函数，封装day5中任务2的代码到刚这个函数下，同时用文档字符串为stats_text_en添加注释说明
def stats_text_en(text):
    ''' 
    以字典形势返回字符串中英文单词的出现频率
    :param text:string
    :return dict:英文单词排序结果
    '''
    # 在这里写具体操作
    mydict={}
    mylist=[]
    mylist=text.split(" ")
    for mylinum in mylist:
        if judge_pure_english(mylinum) and mylinum != "":
            if mylinum in mydict:
                mydict[mylinum]=int(mydict[mylinum])+1
            else:
                mydict[mylinum]=1
    return mydict
print(sorted(stats_text_en(template).items(), key=lambda d: d[1],reverse=True))

#创建一个名为stats_text_cn的函数，该函数的功能是实现统计每个中文汉字出现的次数，同时用文档字符串添加注释说明
def stats_text_cn(text):
    ''' 
    以字典形势返回字符串中文汉字的出现频率
    :param text:string
    :return dict:中文汉字排序结果
    '''
    # 在这里写具体操作
    mydict={}
    text=is_ustr(text).replace(" ","")
    for mylinum in text:
        if mylinum != "":
            if mylinum in mydict:
                mydict[mylinum]=int(mydict[mylinum])+1
            else:
                mydict[mylinum]=1
    return mydict
print(sorted(stats_text_cn(template).items(), key=lambda d: d[1],reverse=True))

def main():
    stats_text_en(template)
    stats_text_cn(template)


if __name__ == '__main__':
    main()






