
#使用字典统计
def stats_text_en(text):
    text=text.replace(',',' ').replace('.',' ').replace('--','').replace('!','').replace('*',' ')#将非英文字符替换为空格
    text=text.lower()#将所有英文字符改为小写
    text=text.split()#以空格拆分为独立的单词
    zidian={}
    for i in text:  #将字符转换为字典
        count=text.count(i)
        r1={i:count}
        zidian.update(r1)
        #print(i,'',count)
    print(zidian)
        
    zidian1=sorted(zidian.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从小到大排序
    print(zidian1)


import re
#统计中文单词
def stats_text_cn(text):      
    result1 = re.findall(u'[\u4e00-\u9fff]+', text)
    newString = ''.join(result1)
    b ={}
    for i in result1:
        b.update({i:newString.count(i)})
    b1 = sorted(b.items(),key = lambda x:x[1],reverse= True)
    print('the result of counting chinese words ', b1, '\n')

def stats_text(test):
    stats_text_en(test)  #统计英文单词
    stats_text_cn(test)  #统计中文单词  

  







