template = '''                       
The Zen of Python, by Tim Peters
美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
可读性计数.
Special cases aren't special enough to 打破规则.
即使练习会使得不再纯粹.
但错误不应该用沉默来掩盖.
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
有且只有一个办法.
Although that way may not be obvious at first unless you're Dutch.
尝试总比从未试过要强.
Although never is often better than *right* now.
如果执行很难被解释，那将是一个很糟的想法.
如果执行很容易解释，这会是一个好点子.
Namespaces are one honking great idea -- 让我们继续为之努力!
'''
def stats_text_en(stri):               #封装 d5_exercise_stats_text.py
    '''【NOTE】：The "stats_text_en()" is importing output result of English words and occurrences): ''' 
    if type(stri) != str:
         raise ValueError("This is not string!")
    endict={}               #新建一个字典
    entext=""               #新建一个空字符串
    stri=stri.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')  #去标点
    #遍历原始字符串
    for i in stri: 
        if i.isascii():         #去掉中文或者说非英文字符
            entext=entext+i     #将英文字符放入新建的字符串中

    entext=entext.split( )      #分隔字符串

    for i in entext:            #遍历新字符串
        endict[i]=entext.count(i)        #创建字典
    endict=sorted(endict.items(),key=lambda item:item[1],reverse=True) #按照值排序，从小到大
    print(stats_text_en. __doc__)
    print(endict)
    return endict         


def stats_text_cn(stri):  
    '''【注】:stats_text_cn()函数为每个汉字统计的次数如下： '''  #用文档字符串注释
    if type(stri) != str:
     raise ValueError("This is not string!")
    dictionary={}                                       #引用一个空字典
    for i in stri:
     if u'\u4e00' <= i <= u'\u9fa5':                    #提取中文汉字   \u是unincode编码，u4e00是十六进制表达值
         dictionary[i]=stri.count(i)
    dictionary=sorted(dictionary.items(),key=lambda item:item[1],reverse = True)      #按照单词出现次数，从大到小排序  
    print(stats_text_cn. __doc__) 
    print(dictionary)
    return dictionary
def main():                                              #输出文档字符串注释，注意：函数和__doc__之间不加()
    stats_text_en(template)
  
    stats_text_cn(template)
   
if __name__ == '__main__':
    main()

#还有一种提取中文的方法如下：

#import re
#def stats_text_cn(str):
#    result = re.findall(u'[\u4e00-\u9fff]+', str)
#    rep = ''.join(result)
#    resoult = {}
#    for i in rep:
#        resoult[i] = rep.count(i)
#    return resoult
#stats_text_cn(str = "")

def stats_text(stri):            #定义stats_text函数
    if type(stri) != str:
     raise ValueError("This is not string!")
    '''注释:

    该函数的功能为：
    调用了两个函数：stats_text_cn(str)和stats_text_cn(str)
    作用是分别统计了英文单词出现的次数，以及中文汉字出现的次数：
    '''
    print(stats_text.__doc__)     #输出注释，注意：__doc__中的下划线'__'需要键盘打两次'_'
    stats_text_en(stri)          
    stats_text_cn(stri)     
   
    