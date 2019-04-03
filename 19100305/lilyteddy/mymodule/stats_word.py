def  stats_text_en(text) :
    if isinstance(text,str):
        text1=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ') #替换分隔符为空格
        text2=text1.split( )#切成单词
        #定义一个dict
        dict={}
        #将x中的每一个单词进行判断，无则赋值，有则赋值+1
        for it in text2:
            
            #是英文的进入下一步处理
            if all(ord(c)<128 for c in it):
                if it not in dict:
                    dict[it] = 1
                else: dict[it] += 1
        #排序，按值，倒序
        dict = sorted(dict.items(),key=lambda x:x[1],reverse=True)
        #返回处理好的dict
        return dict
    else:
        raise ValueError
    




def  stats_text_cn(text) :
    if isinstance(text,str):
        text2=list(text)#切成一个一个字
        #定义一个dict
        dict={}
        #将x中的每一个单词进行判断，无则赋值，有则赋值+1
        for it in text2:
            #是中文的进入下一步处理
            if u'\u4e00'<= it<= u'\u9fff':
                if it not in dict:
                    dict[it] = 1
                else: dict[it] += 1
        #排序，按值，倒序
        dict = sorted(dict.items(),key=lambda x:x[1],reverse=True)
        #返回处理好的dict
        return dict
    else:
        raise ValueError

    

#调用老函数形成新函数
def stats_text(text):
    if isinstance(text,str):
        dict1=stats_text_en(text)
        dict2=stats_text_cn(text)
        #dict3=dict(dict1.items()+dict2.items())
        #print(dict3)
        return (dict1+dict2)
    else:
        raise ValueError

#day8 添加参数类型检查

