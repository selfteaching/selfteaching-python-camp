def stats_text(input):
    result1 =stats_text_en(input)
    print("英文词频----")
    print(result1)
    print("英文词频----")
    result2 =stats_text_en(input)
    print("中文词频----")
    print(result2)
    print("中文词频----")


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


