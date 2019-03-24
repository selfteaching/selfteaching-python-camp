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


# 封装统计英文词频的函数
def stats_text_en(input):
    '''
    参数:input 把想统计的text传入,然后分三个步骤实现
    1.把text 转换成 数组
    2.把数组 清洗一下
    3.把数组转换成字典
    然后把结果返回
    '''
    result =text_to_list(input)
    result =clean_list(result)
    result =statistisc(result)
    return result

def text_to_list(input):
    wordList=input.split()
    return wordList

def clean_list(input):
    for item in input:#清出不必要的符号
        item=item.strip('*-,.')
    return input

def statistisc(input):
    input_dic = {}
    index=0
    for index in range(len(input)):
        input_dic[input[index]]=0
    for index in range(len(input)):
        input_dic[input[index]]=input_dic[input[index]]+1
    return input_dic

def collect_cn(input):
    result =[]
    for item in input:
        words =item.split()
        flag =True
        for singleWord in str(words):
            if(is_chinese(singleWord)):
                flag=True
            else:
                flag=False
    if flag:
        result.append(item)
    return result

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False


#统计中文词频
def stats_text_cn(input):
    #把传入的text 转换成数组
    result =text_to_list(input)
    #删除无用数据
    result =clean_list(result)
    #把含有中文的存入新数组
    result =collect_cn(result)
   
    #用来的方法统计
    result =statistisc(result)
    return result

# re=stats_text_cn(template)
# print(re)
