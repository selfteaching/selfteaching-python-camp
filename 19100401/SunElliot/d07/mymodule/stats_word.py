# Define a function

''' Find the num of every english word in the text'''

def stats_word(text):

        text_simple = text.split() # 去除换行，空格等字符

        text_simple2=[]
        for i in text_simple:
                if i.isalpha():
                        text_simple2.append(i)#去除非单词

        dict1 = {}
        dict1 = dict1.fromkeys(text_simple2)#将text_simple2的元素作为dict1的键值key
        word_1 = list(dict1.keys())
        for i in word_1:
                dict1[i] = text_simple2.count(i)#统计单词出现的次数
        
        dict2 = {}
        dict2 = sorted(dict1.items(),key=lambda d:d[1],reverse=True)#按values进行排序
        dict2 = dict(dict2)#转化为字典
        print(dict2)


''' Find the num of every chinese word in the text'''
def stats_word_cn(text):

        text_simple = text.split() # 去除换行，空格等字符

        text_simple2=[]
        for i in text_simple:
                if u'\u4e00' <= i <= u'\u9fff':
                        text_simple2.append(i)#去除非汉字部分

        dict1 = {}
        dict1 = dict1.fromkeys(text_simple2) #将text_simple2的元素作为dict1的键值key
        word_1 = list(dict1.keys())
        for i in word_1:
                dict1[i] = text_simple2.count(i)#统计汉字出现的次数
        
        dict2 = {}
        dict2 = sorted(dict1.items(),key=lambda d:d[1],reverse=True)#按values进行排序
        dict2 = dict(dict2)#转化为字典
        print(dict2)

''' Find the num of every chinese and english word in the text'''
def stats_text(text):
       stats_word_cn(text)
       stats_word(text)
