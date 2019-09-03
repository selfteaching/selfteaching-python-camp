
import re                     #引入正則表達式 (regular expression)是很方便的字串處理module。用來表達對字符串的一種過濾邏輯。
import collections
count = int()
def stats_text_en(en,count):        #定義一個函數
    #\u4e00-\u9fa5 	漢字的unicode範圍
    #\u0030-\u0039 	數字的unicode範圍
    #\u0041-\u005a 	大寫字母unicode範圍
    #\u0061-\u007a 	小寫字母unicode範圍
    #sub(pattern,repl,string) 	把字符串中的所有匹配表達式pattern中的地方替换成repl, 使用repl替換string中每一個匹配的子串後返回替換後的字符串。
  
    if  isinstance(en,str):
        t1= re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",en) #把en中非英文字符轉換成“ ”
        text1 = t1.split() #把字符串分割
        d = collections.Counter(text1).most_common(count)  #counter 函数自带統計排列功能。返回一個列表，提供 n 個頻率最高的元素和計數。如果沒提供 n ，或者是 None ， most_common() 返回計數器中的 所有 元素。相等個數的元素順序隨機.
        return d
    else:
        raise ValueError("請輸入字符串")

import jieba
def stats_text_cn(cn,count): #定義一個統計中文漢字字頻的函數
    if isinstance(cn,str):
        t2 = re.sub(u"([^\u4e00-\u9fa5])","",cn) #將cn中非中文字符轉換成“”
        t3 = jieba.cut(t2)
        d = collections.Counter(t3).most_common(count)
        return d
    else:
        raise ValueError("請輸入字符串")

def stats_text(j,count): #定義合併輸出函數
    if isinstance(j,str):
       a = stats_text_cn(j,count) + stats_text_en(j,count) #將兩次統計結果合併(中文+英文)
       return a
    else:
        raise ValueError("請輸入字符串")