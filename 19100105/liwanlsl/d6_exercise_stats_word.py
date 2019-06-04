
def stats_text_en():   # 封装统计英文频次的函数
    import d5_exercise_stats_text

text = '扁担长，板凳宽，扁担没有板凳宽，板凳没有扁担长。扁担绑在板凳上，板凳不让扁担绑在板凳上。 '
def annotation(str) ->'这是一个文档':    #添加注释说明
    print('注释：',annotation.__annotations__)

stats_text_en()         
print()


cn_dic={}     #统计中文频次函数
def stats_text_cn(cnstr):
    for i in cnstr: 
        if u'\u4e00' <= i <= u'\u9fa5':
            cn_dic[i]=cnstr.count(i)
    return cn_dic

stats_text_cn(text)       

cn_dic=sorted(cn_dic.items(),key=lambda item:item[1],reverse = True)     
print(cn_dic)      

print() 
annotation(text)          
      