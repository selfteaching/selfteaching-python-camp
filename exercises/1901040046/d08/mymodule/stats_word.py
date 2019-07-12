#将字符串s按照None的分隔切分为一个字符串组，并清洗字符串元素的标点符号，并统计不同字符是数量，最后以数量降序排列。
def stats_text_en(text):
       if type(text) == str:#新增类型检查语句
            replace_text = text.replace(',','').replace('.','').replace('*','').replace('?','').replace('!','').replace('-','')
            split_text = replace_text.split()
            wordcount = {}
            for i in split_text:
               if i not in wordcount:
                  wordcount[i] = 1
               else:
                  wordcount[i] += 1
            wordcount = sorted(wordcount.items(),key=lambda x:x[1],reverse=True) 
            return wordcount
       else:
            raise ValueError('it is not a str.')#如果参数错误，抛出提示。



#定义一个用来统计汉字的函数.新增list函数将中文字符串切分。暂时不引人正则函数从而用来区分中英文。
def stats_text_cn(text):
        if type(text) == str:#新增类型检查语句   
            replace_text = text.replace('，','').replace('。','').replace('*','').replace('？','').replace('！','').replace('——','')
            list_text = list(replace_text)
            wordcount = {}
            for i in list_text:
               if i not in wordcount:
                  wordcount[i] = 1
               else:
                  wordcount[i] += 1
            wordcount = sorted(wordcount.items(),key=lambda x:x[1],reverse=True) 
            return wordcount
        else:
            raise ValueError('it is not a str.')#如果参数错误，抛出提示。


def stats_text(text):#定义函数用来统计并打印中英文字符以及对应数量。
    print(stats_text_en(text))
    print(stats_text_cn(text))

