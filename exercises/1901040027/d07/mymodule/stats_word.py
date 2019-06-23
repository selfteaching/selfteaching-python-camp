
# stats_text module

def stats_text_en(text):
    text = text.replace(',','').replace('.','').replace('--','').replace('*','').replace('!','')#讲非英文字符转化为空
    text = text.lower()#将所有英文字符改为小写
    text = text.split()#以空格拆分独立的单词
    dir1 = {}
    for i in text: #将字符转换为字典
        count = text.count(i)
        r1 = {i:count}
        dir1.update(r1)

    dir2 = sorted(dir1.items(),key = lambda x:x[1],reverse = True)
    print(dir2)



def stats_text_cn(text):
    text = text.replace('\n','').replace('，','').replace('、','').replace(' ','')#删掉换行符，逗号，顿号,空格
    b1 = {} 
    for i in text: #由字符生成字典
        b1.update({i: text.count(i)})

    b2 = sorted(b1.items(),key = lambda x:x[1],reverse = True)
    print(b2)


def stats_text(text):
    stats_text_en(text) #统计英文单词
    stats_text_cn(text) #统计中文单词