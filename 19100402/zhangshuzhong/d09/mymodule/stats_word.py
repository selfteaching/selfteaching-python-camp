
#该函数的功能是统计字符串中英文单词的瓷瓶，并输出单词与单词个数构成的元组字典，
#最后返回一个按词频降序排列的数组
import collections
def stats_text_en(txt,count):
    import re
    if type(txt) == str:#添加字符串参数类型检查（str检查字符串、list检查列表、dict检查字典）
        txt=re.sub('[^A-Za-z]',' ',txt)
        #将文档中的大小写全部换为小写
        txt=txt.lower()
        #将字符串转换为单词列表
        txt=txt.split()
        #开始统计单词列表中单词个数
        print(collections.Counter(txt).most_common(count))
    else:
        raise ValueError('输入参数类型非字符串，请输入字符串')#抛出错误的类型



#该函数用于统计字符串中每个汉字出现的个数。需要输入字符串，输出的结果是按照降序排列的以中文汉字及其字频为元组的一个字典
def stats_text_cn(txt,count):
    import re
    if type(txt) == str:
        txt=re.sub('[^\u4e00-\u9fa5]','',txt)
        #移除字符串头尾的空格和换行符号
        txt=txt.strip()
        print(collections.Counter(txt).most_common(count))
      
        
        
    else:
        raise ValueError('输入参数类型非字符串，请输入字符串')

#该函数用于统计字符串中英文单词与汉字的词频，之后会输出两个字典，分别为以中文汉字及其字频为元组的字典和以英文单词及其词频为元组的字典
def stats_text(txt,count):
    stats_text_cn(txt,count)#汉字字频统计
    stats_text_en(txt,count)#英文单词词频统计
