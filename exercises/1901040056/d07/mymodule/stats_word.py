import re # 调用正则表达式模块，从尖子生哪里学来的
          # re.sub(pattern, repl, string, count=0, flags=0)
def stats_text_en(t_en): # 定义函数
    a = t_en.replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace('--',' ')
    a = a.lower() # 全英文单词小写
    a = re.sub("[^A-Za-z]", " ", a) # 借用了这个正则表达式，这里保留了英文单词，^代表取出大小写a-z以外所有的字符串剔除
    a = a.split() # 分割字符串
    b = {}
    for i in a:
        count =  a.count(i)
        r1 = {i:count} 
        b.update(r1)
    c = sorted(b.items(),key=lambda x:x[1],reverse=True) 
    print('英文单词统计频率如下： \n',c) # 这里print()函数缩进就是封装进我定义的函数里面去了

# 给自己的中文排序函数写个说明
# 1.去标点符号
# 2.定义字典e{}
# 3.用.count（）把中文字符串的字和字频统计出来然后加入字典e
# 4.定义一个参数f，用sorted()函数对f进行排序
# 5.print缩进函数里面就是函数的一个输出参数了
def status_text_cn(t_cn):
    d = t_cn.replace(',','').replace('-',' ').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace(' ','')
    d = re.sub("[A-Za-z0-9]", "",d) #借用了这个正则表达式，这里删除了英文单词，因为没有加上^
    e = {}
    for j in d:
        count = d.count(j)
        r2 = {j:count}
        e.update(r2)
    f = sorted(e.items(),key=lambda x:x[1],reverse=True)
    print('中文单字统计频率如下： \n',f)

def stats_text(tt):
    return(stats_text_en(tt),status_text_cn(tt))