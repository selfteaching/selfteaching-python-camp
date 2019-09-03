
import re                     #引入正則表達式 (regular expression)是很方便的字串處理module。用來表達對字符串的一種過濾邏輯。
def stats_text_en(en):        #定義一個函數
    #\u4e00-\u9fa5 	漢字的unicode範圍
    #\u0030-\u0039 	數字的unicode範圍
    #\u0041-\u005a 	大寫字母unicode範圍
    #\u0061-\u007a 	小寫字母unicode範圍
    #sub(pattern,repl,string) 	把字符串中的所有匹配表達式pattern中的地方替换成repl, 使用repl替換string中每一個匹配的子串後返回替換後的字符串。
  
    if  isinstance(en,str):
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
    else:
        raise ValueError("請輸入字符串")

def stats_text_cn(cn): #定義一個統計中文漢字字頻的函數
    if isinstance(cn,str):
        t2 = re.sub(u"([^\u4e00-\u9fa5])","",cn) #將cn中非中文字符轉換成“”
        d = {}
        for i in t2:     #中文不需要分割，可以直接循環一遍！
            if i in d:
                d[i] +=1 #如果字典中沒有就顯示1，有的話就在原來的基礎上+1
            else:
                d[i] =1
        a = sorted(d.items(),key=lambda x:x[1],reverse = True) #利用lambda函數進行values值的排序
        return a
    else:
        raise ValueError("請輸入字符串")

def stats_text(j): #定義合併輸出函數
    if isinstance(j,str):
       a = stats_text_cn(j) + stats_text_en(j) #將兩次統計結果合併(中文+英文)
       return a
    else:
        raise ValueError("請輸入字符串")