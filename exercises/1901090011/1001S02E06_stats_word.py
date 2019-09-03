text = '''
The Zen of Python, by Tim Peters 


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
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!
美麗比醜陋好,
明確比晦澀好!
'''
import re                     #引入正則表達式 (regular expression)是很方便的字串處理module。用來表達對字符串的一種過濾邏輯。
def stats_text_en(en):        #定義一個函數
    #\u4e00-\u9fa5 	漢字的unicode範圍
    #\u0030-\u0039 	數字的unicode範圍
    #\u0041-\u005a 	大寫字母unicode範圍
    #\u0061-\u007a 	小寫字母unicode範圍
    #sub(pattern,repl,string) 	把字符串中的所有匹配表達式pattern中的地方替换成repl, 使用repl替換string中每一個匹配的子串後返回替換後的字符串。
    t1= re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",en) #把en中非英文字符轉換成“ ”
    text1 = t1.split() #把字符串分割
    d = {} #建一個空字典
    for i in text1: #循環一遍
        if i in d:
            d[i] += 1 #如果字典中沒有就顯示1，有的話就在原來的基礎上+1
        else:
            d[i] = 1

    a = sorted(d.items(),key=lambda x:x[1],reverse = True) #利用lambda函數進行values值的排序 (lambda 函數是一種快速定義單行的最小函數)
    return a
print(stats_text_en(text))

def stats_text_cn(cn): #定義一個統計中文漢字字頻的函數
    t2 = re.sub(u"([^\u4e00-\u9fa5])","",cn) #將cn中非中文字符轉換成“”
    d = {} #建一個空字典
    for i in t2:     #中文不需要分割，可以直接循環一遍！
        if i in d:
            d[i] +=1 #如果字典中沒有就顯示1，有的話就在原來的基礎上+1
        else:
            d[i] =1
    a = sorted(d.items(),key=lambda x:x[1],reverse = True) #利用lambda函數進行values值的排序
    return a
print(stats_text_cn(text))
