text='''It is the time you have wasted for your rose that makes your rose so important.
你在你的玫瑰花身上耗费的时间,使得你的玫瑰花变得如此重要!!!!!!!!!!!!!
And no grown-ups will ever understand that this is a matter of so much importance！
但是，大人们永远也不会了解这件事有多么重要！
His flower had told him that she was only one of her kind in all universe。 And here were five thousand of them， all alike， in one single garden！
他的花朵曾经告诉他，自己是宇宙间仅有的一种花；可是仅仅在这座花园里，就有五千朵和她一模一样的花！
What moves me so deeply， about this little prince who is sleeping here， is his loyalty to a flower – the image of a rose that shine through his whole being like the flame of a lamp， even when he is asleep…
这个熟睡的小王子最叫我感动的地方是，他对一朵玫瑰的感情——甚至他睡着了，那朵玫瑰花的影子，仍像灯光一样照亮他的生命……
中文字符测试：《》、「」【】#@%……&*
英文字符测试：,./';[:"?>]
'''
import re#导入正则表达式模块
def stats_text_en():
    global text #把text标记为全局变量
    found = {}#建立空的字典
    a= text.lower()
    a=re.sub("[^\\u0061-\u007a]", " ", a)#小写字母unicode范围，筛选英文
    a=a.split()#指定分隔符对字符串进行切片
    
    for i in a:
        if i  in found:
            found[i]+=1
        else:
            found[i]=0
            found[i]+=1
    print('英文单词统计结果：',sorted(found.items(),key=lambda x:x[1],reverse=True))#词频降序
 
stats_text_en()




#统计中文词频
import re
def stats_text_cn():
    global text #把text标记为全局变量
    found={}

    #提取中文字符串
    text= re.sub("[^\u4e00-\u9fa5]", "", text)#中文汉字unicode范围
    text=text.replace( "  ",'').replace("\n",'')
    print(text)

    for i in text:
        if i  in found:
            found[i]+=1
        else:
            found[i]=0
            found[i]+=1

    print('中文汉字字频统计结果： ',sorted(found.items(),key=lambda x:x[1],reverse=True))

stats_text_cn()



   
