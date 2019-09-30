en_text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 
Flat is better than nested. Sparse is better than dense. Readability counts.
Special cases aren't special enough to break the rules. Although practicality beats purity. 
Errors should never pass silently.
Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!'''

cn_text = '''

第2季（共10集）
据悉，新一季背景将部分设定在二战期间日裔美国人拘留营
“从南加州的家乡到拘留营再到太平洋战场的前线，一种神秘怪物恐吓着一个日裔美国人社区。”
该系列的主创之一Alexander Woo将担任新一季的剧集运作人。他本人也在第一时间发表了如下声明：
“我倍感荣幸能有机会讲述这样一个非常时期的特殊故事
我们希望能将这种历史经历带来的不幸恐惧以一种紧扣当下现实的方式呈现出来
能有大部分亚裔以及亚裔美国人的参与是一件令人兴奋又让人谦虚的事。”
《极地恶灵》第1季于3月份登陆AMC
围绕19世纪40年代英国皇家海军惊恐号探索北极圈“西北航道”的故事展开。
年回归，具体日期和演员招募有待官宣
'''

#定义一个名为stars_text_en的函数，函数接受一个字符串text作为参数。

def stars_text_en (text):
   
    
    elements = text.split()


    words = []



    symbols = ',.*-!'

    for element in elements:

        for symbol in symbols:
    
            element = element . replace(symbols,'')
     
        if len(element):
            words.append(element)

    


    counter = {}


    word_set = set (words)

    for word in word_set: 
        counter [word] = words.count(word)
    return sorted(counter.items(), key = lambda x:x[1],reverse=True)



    #统计参数中每个汉字出现的次数
    def stars_text_cn(text):
        cn_characters = []
        for charcters in text:
            #unicode的中文取值范围
            if '\u4e00' <= character <= '\u9fff':
                cn_charcters.append(characters)
        counter = {}
        cn_charaters_set = set(cn_charcters)
        for characters in cn_charaters_set:
            counter [characters] = cn_cheraters.count(characters)
        return sorted(count.items(), key = lambda x:x[1],reverse = True)



    #搜索 __name__==__main__
    #一般情况下在文件内测试代码的时候以下面的形式进行
    if __name__ == "__main__":
        en_result = stars_text_en(en_text)
        cn_result = stars_text_cn(cn_text)
        print('统计参数中每个英文单词出现的次数 ==>\n',en_result)
        print('统计参数中每个中文单词出现的次数 ==>\n',cn_result)
            

