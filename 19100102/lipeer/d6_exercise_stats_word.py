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

#将字符串s按照None的分隔切分为一个字符串组，并清洗字符串元素的标点符号
def cut_and_clean(s):
    #切分字符串
    s=s.split()
    #清洗标点符号
    i=0
    while i<len(s):
        s[i]=s[i].strip('*-.')
        if s[i]=='': #清洗完成之后若为空元素‘’，则删除元素
            s.remove('')
        else:
            i=i+1
    return s

#除去非英文字符串
#可能的BUG是：英文和中文连在一起，则不被收录
def english_only(str_list):
    en_list = []
    i=0
    for i in range(len(str_list)): #确认是英文单词之后填补en_list
        for j in range(len(str_list[i])): #确认每个字符都是英文
            if not ( str_list[i][j]<'z' and str_list[i][j]>'a' ) or ( str_list[i][j]<'Z' and str_list[i][j]>'A' ):
                j=-1
                break
        if j!=-1:
            en_list += [str_list[i]] #如果所有字符都是英文，则填补列表
    return en_list

#除去非中文字符串
def chinese_only(string):
    chinese_str=''
    for i in range(len(string)):
        #可能的BUG是：超出了基本汉字集的汉字（如汉字补充、汉字偏旁部首等）不会被收录
        if ord(string[i])>19968 and ord(string[i])<40869: #基本汉字的unicode编码范围
            chinese_str += string[i]
    return chinese_str
            

#把list转化为dict并统计词频
def list_to_dict_and_cal(aList):
    aDict={}
    for i in range(len(aList)): #把list转化dict
        aDict[aList[i]]=0
    for i in range(len(aList)): #统计词频
        aDict[aList[i]]=aDict[aList[i]]+1
    return aDict

def stats_text_en(text, print_text=False):
    """统计英文单词词频并按词频从高到低排序
    
    Parameter:
    text -- 即将被处理的文本，必须为字符串
    Keyword Argument:
    print_text -- 选择是否打印结果，默认为False不打印结果
    Return Value:
    返回一个字典，key为单词字符串，value为词频
    Potential Bug:
    若英文字符和中文字符连在一起，则不被字典收录
    """
    text = cut_and_clean(text) #切分字符串并清洗标点符号
    text = english_only(text) #除去非英文字符串
    text_dict = list_to_dict_and_cal(text) #将text转化为字典并统计词频
    text_dict = sorted(text_dict.items(),key=lambda item:item[1],reverse=True) #对字典按照value值排序
    if print_text: #如果要求打印，则打印结果
        print(text_dict)
    return text_dict

def stats_text_cn(text, print_text=False):
    """统计中文字字频并按字频从高到低排序
    
    Parameter:
    text -- 即将被处理的文本，必须为字符串
    Keyword Argument:
    print_text -- 选择是否打印结果，默认为False不打印结果
    Return Value:
    返回一个字典，key为汉字字符，value为字频
    Potential Bug:
    超出了基本汉字集的汉字（如汉字补充、汉字偏旁部首等）不会被字典收录
    """
    text = chinese_only(text)
    text = list(text) #将中文字符串转换为中文列表
    text_dict = list_to_dict_and_cal(text) #统计中文字频
    text_dict = sorted(text_dict.items(),key=lambda item:item[1],reverse=True) #对字典按照value值排序
    if print_text: #如果要求打印，则打印结果
        print(text_dict)
    return text_dict

def main():
    stats_text_en(template, print_text=True)
    stats_text_cn(template, print_text=True)

if __name__ == '__main__':
    main()