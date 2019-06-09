t='''
'''
t1=t.replace(',',' ').replace('！',' ').replace.('*',' ').replace('.',' ')
t2=t1.lower()
t3=t2.split()
word_dict={}
    for i in t3:
        c=t3.count(i)
        t4={i:c}
        word_dict.update(t4)
print(word_dict)

wd1=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
print(wd1)
