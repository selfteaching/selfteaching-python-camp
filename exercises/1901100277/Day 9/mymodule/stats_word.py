
def stats_text_en (en_text) :
    ''' 统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组'''

    #如果不是字符串，抛异常，异常会终止代码执行
    if not isinstance(en_text, str):
        raise ValueError("非字符串格式，请重新输入")
    
    new = en_text.split(" ") #分割字符串，变为列表,以空格进行分割

    words = [] 

    symbols = ",.*-!@\n"    

    for new1 in new :   # 遍历首次分割后单词

        for symbol in symbols :  # 遍历要剔除的符号
            new1 = new1.replace(symbol,"")  # 如果粗糙单词里有这个符号,就将符号 替换为空
        if len(new1) >0 :  # 替换后如果 元素长度大于零,说明是有效单词
            words.append(new1)  # 把他添加到words 列表里


    # 使用 collections 模块里的 counter函数 进行词频统计 
    
    from collections import Counter
    n = int(input("请输入 您需要显示出现词频最高的前多少个词? >>> :"))
    return dict(Counter(words).most_common(n))


################################################################################
################################################################################

# 统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组

def stats_text_cn (cn_text) :
    ''' 统计参数中每个汉字出现的次数，最后返回一个按词频降序排列的数组'''

    #如果不是字符串，抛异常，异常会终止代码执行
    if not isinstance(cn_text, str):
        raise ValueError("非字符串格式，请重新输入")

    # text = str(cn_text)
    # new = list (text) #汉字 字符串可以直接用 list 转化为 单个文字的列表.

    words = []                             # 定义一个新列表,存储去掉符号后的新列表

    symbols = "！？｡＂＃＄％＆＇ （）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏." 

    for wen_zi in cn_text :  # i 就是文章里的某个元素
        if  "\u4e00" <= wen_zi <=  "\u9fff" : # unicode 中 中文字符的 范围 (包括中文标点符号)   如果元素是中文
            for symbol in symbols :        # 遍历要剔除的标点符号
                wen_zi1 = wen_zi.replace(symbol,"")   
            words.append(wen_zi1)          # 把他添加到words 列表里  

    from collections import Counter
    n = int(input("请输入 您需要显示出现词频最高的前多少个词? >>> :"))
    return dict(Counter(words).most_common(n)) 

    #################################################

def stats_text(string):
    '''
    统计 英文单词字频 和中文字频 的结果,并按从大到小排列
    '''

    #如果不是字符串，抛异常，异常会终止代码执行
    if not isinstance(string, str):
        raise ValueError("非字符串格式，请重新输入")

    return stats_text_en(en_text) + stats_text_cn(cn_text)





