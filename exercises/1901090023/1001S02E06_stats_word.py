# 1. 封装统计英文单词词频的函数
text='''You have found the career you are passionate about and good at; 
you have found Ms/r Right worthy of your entire life to be with and grow together; 
you have found the community that has passion for the same goal; 
you have found a couple of open-minded and trustworthy friends.'''     

# 定义函数
def stats_text_en(text):                   # 定义函数，形式参数名为text
    """ 函数名：stats_text_en               # 文档字符串用来为函数添加注释说明

    参数名：text
    统计参数中英文单词词频
    最后返回一个按词频降序排列的数组
    """
    
    text1 = text.replace(';', '').replace('.', '')     # 去掉字符串中的特殊符号
    list1 = text1.split()                              # 字符串转换为列表
   
    d={}                                               # 创建一个空字典d
    for i in list1:                                    # for循环遍历列表, i 为列表中的各个元素
        d[i]=list1.count(i)                            # list1.count(i)是i 单词元素在列表中的次数，将其赋值给字典d中key为i单词元素的value值
    d1=sorted(d.items(),key=lambda x:x[1],reverse=True) # items() 函数以列表返回可遍历的(键, 值) 元组数组；sorted()函数，通过key参数，指定第二个字段（value值）的值的降序来排序
    return d1                                           # python 函数返回值 return，函数中一定要有return返回值才是完整的函数。              【非常重要】

# 执行函数
print("英文单词及出现次数降序排列")
print(stats_text_en(text))                              
print('_'*200)


# 2. 封装统计中文汉字字频的函数
text= '''
找到了那份热爱且擅长的事业。
找到了值得相守一生、共同成长的伴侣。
找到了志同道合、精神饱满的社群。
找到了敞亮明朗靠谱的二三好友。
'''

def stats_text_cn(text:str) -> dict:         # 定义函数，用来统计中文汉字字频，并且给函数名添加注释说明
    """ 函数名：stats_text_cn                 # 文档字符串用来为函数添加注释说明

    参数名：text
    统计参数中中文汉字词频
    最后返回一个按词频降序排列的数组
    """

    text = text.replace('。','').replace('、','').replace('', ' ')    # 前两个去掉特殊符号，最后一个是把字符串拆成一个个汉字 【非常重要】
    list1 = text.split()                    # 将字符串转换为列表

    from collections import Counter          # collections模块下的Counter计算器
    c = Counter(list1)                       # Counter对象（记住，是dict的子类）的key是待计数元素，value是对应的计数
    return (c)                               # python 函数返回值 return，函数中一定要有return返回值才是完整的函数。         【非常重要】
                                             # 如果没有python 定义函数返回值，那么会得到一个结果是None对象，而None表示没有任何值。

print("中文汉字及出现次数降序排列")
print(stats_text_cn(text))
print('_'*200)