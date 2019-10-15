from collections import Counter
#####################     1.输出英文函数
def stats_text_en(text):        #定义函数
    #统计参数中每个英⽂文单词出现的次数，最后返回⼀一个按词频降序排列列的数组
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s'% type(text))
    ######处理生成纯英文单词列表
    words = []
    elements = text.split()
    symbols = ',.*!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
            element.strip()

        words.append(element)   
      
    return words


######################   2.输出中文函数
def stats_text_cn(text_cn):
    #统计参数中每个中文汉字出现的次数
    if not isinstance(text_cn,str):
        raise ValueError('参数必须是 str 类型，输入类型%s'% type(text_cn))

    cn_char= []
    for char in text_cn:
        cn_char.append(char)
    
    symbols = ',，.*!'    ##########汉字拼写下的“，”与拼音状态下的“,”不同
    for symbol in symbols:
        if symbol in cn_char:
            cn_char.remove(symbol)

    return cn_char

text1= 'hello world! hello every one!'     
text2 = '中国共产党万岁，中国人民万岁'

#######    3.Counter()计数器输出
word_union = stats_text_en(text1)+stats_text_cn(text2)
cnt = Counter()
for word in word_union:
    cnt[word] += 1

print(cnt.most_common())  ######全部输出
count = 4
print(cnt.most_common(count))       ###输入前四

##############   4.读取本地文件   ##########绝对路径的 /  需要改为   \
with open('c:/Users/sddl/Documents/GitHub/selfteaching-python-camp/exercises/1901100303/d09/mymodule/tang300.json',encoding='utf-8') as ff:
    read_data = ff.read()

print(len(read_data))
tang_list = []
for tang_char in read_data:
    if '\u4e00' <= tang_char >= '\u9fff':
        tang_list.append(tang_char)

tang_cnt = Counter()
for word in tang_list:
    tang_cnt[word] += 1

print(tang_cnt.most_common(100))      #输出词频前100

