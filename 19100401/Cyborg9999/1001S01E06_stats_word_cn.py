text_cn = '''
 “没有时间了”，是“时间恐慌症”患者脑子里唯一反复闪现的一句话。巨大的压力，极度的恐惧，使患者的身上集结并综合了一切矛盾：
他们既勤奋又懒惰，既聪明又愚蠢，既勇敢又懦弱，既满怀希望又时时刻刻面临绝望，既充满自信又随时随地体会卑微……
“没有时间了”，其可怕程度几乎无异于死亡。死亡是所有人最终都要面临的终极困境——没有解决方案的困境。
对其恐惧之甚，乃至于人类不分种群、不约而同地集体创造出一个天堂留给自己和自己喜爱的人们，
同时还另外造了一个地狱送给他们所憎恨的人们。但这毕竟并不是切实有效的解决方案。
死亡本身其实并不可怕，面临死亡的过程才真正可怕。如此看来，很容易想象那些“既勤奋又懒惰”的学生面临的是怎样悲惨的境遇。”
'''



def stats_text_cn(string):
    import re #导入正则表达式模块
    result_cn_interpunction = re.sub('[^\u4e00-\u9fa5]','',string) #提取中文字符串
    string = string.replace(' ','').replace('\n','')#删除空元素与换行元素
    list1 = re.split('',string) #将字符串转换为列表list1
    dict1 = {} #建立字典
    for i in list1: #i值开始遍历文本
        dict1.setdefault(i,list1.count(i)) #将列表中的汉字及汉字的出现次数，分别赋值给dict1的键和值
    tup1 = sorted(dict1.items(),key = lambda x:x[1],reverse = True)#将dict1按照value值从大到小排列，并将结果赋值给tup1
    return tup1#返回值

print(stats_text_cn(text_cn))
