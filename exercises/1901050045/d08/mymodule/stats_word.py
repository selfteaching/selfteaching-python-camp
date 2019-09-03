def stats_text_en(text):        #定义函数
        if type(text)!= str:
                raise ValueError('参数输入错误,请输入字符串')
        text=text.split()       #将text列表化
        h=[]                    #定义h列表
        for x in text:          #将text中的英文单词添加到h列表中
                if x.isalpha():
                        h.append(x)    
        seta=set(h)             #设定集合a
        b=[]                    #定义b列表
        for i in seta:          
                count=h.count(i)#重复次数                             
                a=(i,count)     #a=(单词名，重复次数)
                b.append(a)     #将a添加到b                                            
        b=sorted(b,key=lambda kv:kv[1], reverse=True)       #由大到小排序
                                                   #将b设置成字典
        return b                                           



#=================================================================任务2================================================================

def stats_text_cn(text):
        if type(text)!=str:
                raise ValueError('参数输入错误,请输入字符串')
        text = text.replace(',',' ').replace('.',' ').replace('\'','').replace('-',' ').replace('!',' ').replace('*',' ')#去标点符号
        setb=set(text)                                 #设定集合
        x=[]                                            #设定x列表
        for o in setb:                                  #o从集合setb中取
                if o >= u'\u4e00' and o <= u'\u9fa5':#如果o是在u4e00 到u9fa5之间（汉字）
                        count=text.count(o)#统计每个汉字的数量
                        y=(o,count)
                        x.append(y)#将y加到x列表中
        x=sorted(x,key=lambda kv:kv[1],reverse=True)#按重复次数，由大到小排列
        
        return x



def stats_text(text):
        if type(text) != str:
                raise ValueError('参数输入错误,请输入字符串')
        print(stats_text_en(text)+stats_text_cn(text))

        






