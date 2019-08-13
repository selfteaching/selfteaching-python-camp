#以待处理文件作为参数定义一个函数，将待处理文件split成字符串list并命名，对新的list做处理，然后生成一个element.list，
#即完成待处理文件的加工，得到一个符合条件的完整list.words，第三步，创建空白字典{}，对第二步得到的完整words做set处理，
#得到没有重复信息的list.Word-set; 然后count每个word的出现次数。第四步，返回打印出列表
#总：对原始数据做字符串list处理，剔除不和要求的字符串（非单词),创建字典，set单词汇总，count统计单词出现次数，Sorted出来
# 定义函数后，处理函数，return, 用if -name-main做测试，print出来


#定义函数 stats_text_en, 且‘text’为参数
def stats_text_en(text):  
    #将原始文件切割成字符串list并赋值到为elements
    elements=text.split() 
    #建立一个新的空白list类型变量
    words=[]  
    #对symbols赋值
    symbols='* . - ! ,' 
    #for循环  定义变量 element 在 list elements中
    for element in elements: 
        for symbol in symbols: 
            #发现symbol中的值就用空格替代，并返回为element,此目的是清除掉特殊字符
            element=element.replace(symbol,'') 
            #element的长度大于零，表示是我们要的字符
        if len(element):     
            #将符合上条要求的字符加入words list中
            words.append(element)  

    #创建空白字典，命名为counter
    counter={}    

    #把words list中的字符串做一个唯一的集合
    word_set=set(words)  
    for word in word_set:  
        #count 每个Word在words中出现的次数，并返回给counter[word]
        counter[word]=words.count(word) 
    #函数要用return,做返回, reverse=Ture表示降序排列,sorted表示按照要求打印出字典counter列表
    return sorted(counter.items(), key=lambda X : X[1],reverse=True)  
         


def stats_text_cn(text): 
    cn_characters=[]
    for character in text:  
        if '\u4e00'<= character <= '\u9fff': #汉字的字符串代码
            cn_characters.append(character)

    counter={}
    cn_characters_set=set(cn_characters)
    for character in cn_characters_set:
        counter[character]=cn_characters.count(character) #count 每个Word在words中出现的次数，并返回给counter[word]

    return sorted(counter.items(), key=lambda X : X[1],reverse=True)
    



en_text='''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''


cn_text='''
大江东去浪淘尽
千古风流人物故垒西边
人道是三国周郎赤壁
乱石穿空惊涛拍岸卷起千堆雪
江山如画一时多少豪杰
遥想公瑾当年小乔初嫁了雄姿英发羽扇纶巾谈笑间樯橹灰飞烟灭
故国神游多情应笑我早生华发
人生如梦一尊还酹江月
'''

if __name__ == "__main__":  #用此形式，做测试代码，以便以后调用，
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数 ==>\n',en_result)
    print('统计参数中每个中文汉字出现的次数 ==>\n',cn_result)