

#统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组

def stats_text_en (en_text) :
    ''' 统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组'''
    text = str(en_text)
    new = text.split(" ") #分割字符串，变为列表,以空格进行分割。

    words = []  # 定义一个新列表,存储去掉符号后的新列表


    #先针对样本文本挑选出需要剔除的非单词符号
    symbols = ",.*-!@\n"    # 经过观察里面 有这几种符号 我们不需要.

    for new1 in new :   # 遍历分割后的粗糙单词

        for symbol in symbols :  # 遍历要剔除的符号
            new1 = new1.replace(symbol,"")  # 如果粗糙单词里有这个符号,就将符号 替换为空
        if len(new1) >0 :  # 替换后如果 元素长度大于零,说明是有效单词
            words.append(new1)  # 把他添加到words 列表里
    print("去除各种符号后 有效的单词 为这些>>>:",words) 


    print("统计单词出现次数：")
    d ={} #这里要用大括号
    for i in words :    
        j= new.count(i)     # 一个元素出现的: 次数 ,此处的i 就表示一个单词,上面已经分割好;另外用法 也可以是一个字符串中的 某一个或者几个字母,比如 'ea'
        d[i] = j # 这里就是把这个单词 和 出现的次数 添加到 字典中,当然也可以用 update 函数 
        #   d={i:j} #这里要用大括号

    print(d)

    print("将单词 按出现频次数从大到小输出：")  
    # sorted 函数 排序:https://docs.python.org/zh-cn/3/howto/sorting.html#sortinghowto
    d1=sorted(d.items(),key=lambda x:x[1],reverse=True)   
    return d1

en_text = "the hao de wo kan xing xing wo wo @"   # 需要处理的英文单词
aa = stats_text_en(en_text)       # 调用函数
print(aa)  



# 统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组

def stats_text_cn (cn_text) :
    ''' 统计参数中每个汉字出现的次数，最后返回一个按词频降序排列的数组'''
    text = str(cn_text)
    new = list (text) #汉字 字符串可以直接用 list 转化为 单个文字的列表

    words = []  # 定义一个新列表,存储去掉符号后的新列表


    #先针对样本文本挑选出需要剔除的非单词符号
    symbols = "！？｡＂＃＄％＆＇ （）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."    # 经过观察里面 有这几种符号 我们不需要.

    for new1 in new :   # 遍历分割后的粗糙单词

        for symbol in symbols :  # 遍历要剔除的符号
            new1 = new1.replace(symbol,"")  # 如果粗糙单词里有这个符号,就将符号 替换为空
        if len(new1) >0 :  # 替换后如果 元素长度大于零,说明是有效单词
            words.append(new1)  # 把他添加到words 列表里
    print("去除各种符号后 有效的文字 为这些>>>:",words) 

    print("统计单个文字出现次数：")
    d ={} #这里要用大括号
    for i in words :    
        j= new.count(i)     # 一个元素出现的: 次数 ,此处的i 就表示一个单词,上面已经分割好;另外用法 也可以是一个字符串中的 某一个或者几个字母,比如 'ea'
        d[i] = j # 这里就是把这个单词 和 出现的次数 添加到 字典中,当然也可以用 update 函数 
        #   d={i:j} #这里要用大括号

    print(d)

    print("将文字 按出现频次数从大到小输出：")  
    # sorted 函数 排序:https://docs.python.org/zh-cn/3/howto/sorting.html#sortinghowto
    d1=sorted(d.items(),key=lambda x:x[1],reverse=True)   
    return d1


cn_text = "测试：今天是个好日子，126456220600 ，心想的事儿都能成，哈哈哈，都能成＃＄％＆＇（）＊＋，－／" # 中文文字
bb = stats_text_cn(cn_text)  # 调用函数
print(bb)

