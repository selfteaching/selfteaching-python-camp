import typing
import os
import sys
import json
import jieba

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

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# 将字符串s按照None的分隔切分为一个字符串组，并清洗字符串元素的标点符号
def cut_and_clean(s):
    # 切分字符串
    s=s.split()
    # 清洗标点符号
    i=0
    while i<len(s):
        s[i]=s[i].strip('*-.')
        if s[i]=='': # 清洗完成之后若为空元素‘’，则删除元素
            s.remove('')
        else:
            i=i+1
    return s

# 除去非英文字符串
# 可能的BUG是：英文和中文连在一起，则不被收录
def english_only(str_list):
    en_list = []
    i=0
    for i in range(len(str_list)): # 确认是英文单词之后填补en_list
        for j in range(len(str_list[i])): # 确认每个字符都是英文
            if not ( str_list[i][j]<'z' and str_list[i][j]>'a' ) or ( str_list[i][j]<'Z' and str_list[i][j]>'A' ):
                j=-1
                break
        if j!=-1:
            en_list += [str_list[i]] # 如果所有字符都是英文，则填补列表
    return en_list

# 除去非中文字符串
def chinese_only(string):
    chinese_str=''
    for i in range(len(string)):
        # 可能的BUG是：超出了基本汉字集的汉字（如汉字补充、汉字偏旁部首等）不会被收录
        if ord(string[i])>19968 and ord(string[i])<40869: # 基本汉字的unicode编码范围
            chinese_str += string[i]
    return chinese_str


# 把list转化为dict并统计词频
def list_to_dict_and_cal(aList):
    aDict={}
    for i in range(len(aList)): # 把list转化dict
        aDict[aList[i]]=0
    for i in range(len(aList)): # 统计词频
        aDict[aList[i]]=aDict[aList[i]]+1
    return aDict

def stats_text_en(text, count=10, print_text=False):
    """统计英文单词词频并按词频从高到低排序
    Parameter:
    text -- 即将被处理的文本，必须为字符串
    Keyword Argument:
    print_text -- 选择是否打印结果，默认为False不打印结果
    count -- 输出元素的个数，默认为10个。若count<=0则全部打印。必须为int类型
    Return Value:
    返回一个字典，key为单词字符串，value为词频
    Potential Bug:
    若英文字符和中文字符连在一起，则不被字典收录
    """
    if not isinstance(count,int): # 检查count是否为int类型
        raise TypeError('count should be int!')

    if not isinstance(text,str): # 检查text是否为字符串类型
        raise ValueError('It\'s not a string!')
    text = cut_and_clean(text) # 切分字符串并清洗标点符号
    text = english_only(text) # 除去非英文字符串
    if count<=0: #用老方法全部打印
        text_dict = list_to_dict_and_cal(text) #将text转化为字典并统计词频
        text_dict = sorted(text_dict.items(),key=lambda item:item[1],reverse=True) #对字典按照value值排序
    else: #利用typing里的Counter处理文本
        text_dict = typing.Counter(text).most_common(count)
    if print_text: # 如果要求打印，则打印结果
        print(text_dict)
    return text_dict

def stats_text_cn(text, count=10, print_text=False):
    """统计中文字字频并按字频从高到低排序
    Parameter:
    text -- 即将被处理的文本，必须为字符串
    Keyword Argument:
    print_text -- 选择是否打印结果，默认为False不打印结果
    count -- 输出元素的个数，默认为10个。若count<=0则全部打印。必须为int类型
    Return Value:
    返回一个字典，key为汉字字符，value为字频
    Potential Bug:
    超出了基本汉字集的汉字（如汉字补充、汉字偏旁部首等）不会被字典收录
    """
    if not isinstance(count,int): #检查count是否为int类型
        raise TypeError('count should be int!')

    if not isinstance(text,str): #检查text是否为字符串类型
        raise ValueError('It\'s not a string!')
    # text = chinese_only(text) #只留下中文字符
    text = [x for x in jieba.cut(text) if len(x) >= 2] #利用jieba库的cut函数来处理文本，输出长度大于等于2的中文
    if count<=0: #用老方法全部打印
        text = list(text) #将中文字符串转换为中文列表
        text_dict = list_to_dict_and_cal(text) #统计中文字频
        text_dict = sorted(text_dict.items(),key=lambda item:item[1],reverse=True) #对字典按照value值排序
    else: #利用typing里的Counter处理文本
        text_dict = typing.Counter(text).most_common(count)
    if print_text: # 如果要求打印，则打印结果
        print(text_dict)
    return text_dict

def stats_text(text, count=0, en_first=True):
    """统计中英文词频并按词频从高到低排序之后输出
    Parameter:
    text -- 即将被处理的文本，必须为字符串
    Keyword Argument:
    en_first -- 选择是否将英文字典排列在前面，默认为True将英文字典排列在前面
    count -- 输出元素的个数，默认为10个。若count<=0则全部打印。必须为int类型
    Return Value:
    没有返回值
    Potential Bugs:
    1.超出了基本汉字集的汉字（如汉字补充、汉字偏旁部首等）不会被字典收录
    2.若英文字符和中文字符连在一起，则不被字典收录
    """
    if not isinstance(text,str):
        raise ValueError('It\'s not a string!')
    if en_first:
        print(stats_text_en(text, count=count) + stats_text_cn(text, count=count))
    else:
        print(stats_text_cn(text, count=count) + stats_text_en(text, count=count))

def main():
    #stats_text_en(template, print_text=True)
    #stats_text_cn(template, print_text=True)

    location = sys.argv[0] #获取main.py的路径
    location = location.rstrip('stats_word.py') + 'tang300.json' #获取tang300.json的路径

    with open(location,'r',encoding='UTF-8') as tang_text: #读取文件
        text = json.load(tang_text) #json转码
        text_all='' #初始化contents的容器
        for i in range(len(text)): #往容器里填contents
            text_all+=text[i]['contents'] #得到一个由contents组成的字符串
        stats_text_cn(text_all, count=100, print_text=True)
        #调用函数统计并打印100个字频最高的字，修改count的值可以修改打印的字数

if __name__ == '__main__':
    main()