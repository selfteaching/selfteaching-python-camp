'''import jieba
import collections
# 函数2：统计输入文本中中文字的词频：
def stats_text_cn(text):  
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    
    text1 = []
    for i in text:  # 这个循环有效，说明一串汉字也是一个字符串，每个汉字就是其中的一个元素，可以用for in 来遍历，其中i代表了每个汉字的unicode编码
        if i <u'\u4e00' or > u'\u9fff':     # 挑选出非中文字
            text=text.split(i,"") # 将非中文字符删除
    seg_list = jieba.cut(text,cut_all =False)
    
    for j in seg_list:
             if len(j) >= 2 : #只统计长度大于等于2的词
              text1.append(j)
    count = int(input('请输入要限制输出的元素个数：'))
    text1 = collections.Counter(text1).most_common(count)  #按出现次数从大到小排列
    return text1
    
with open('tang300.json','r',encoding='UTF-8') as f:
    a = f.read()
try:
    if not isinstance(a,str):
        raise ValueError()
    
except ValueError:
    print('输入的不是文本格式，请重新输入：')   
    
print(stats_text_cn(a))'''

'''
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA', auth=('linlinya@gmail.com', 'yWt590109'))
r.status_code
200
r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text
u'{"type":"User"...'
r.json()
{u'disk_usage': 368627, u'private_gists': 484, ...}

print r.status_code
print r.headers['content-type']'''


'''# 函数3：统计中英文混合词频：
def stats_text(text):
    
    dic_1 = stats_text_cn(text) # 调用函数1统计中文字词频
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':
            text = text.replace(i,"") #删除所有中文字
    text = text.replace('「', '').replace('」', '').replace('，', '').replace('。', '').replace('：', '').replace('？', '').replace('！', '')
    # 以上一句删除所有中文标点
    dic_2 = stats_text_en(text) # 调用2函数统计英文单词词频
    dic_3 = {}
    dic_3.update(dic_2)
    dic_3.update(dic_1) # 将之前分别得到的两个中英文词频结果字典合并
    dic_3 = sorted(dic_3.items(),key = lambda x:x[1],reverse = True) # 对合并后的字典进行排序，得出混合排序结果

    return(dic_3) '''
import jieba
import collections
    # 函数2：统计输入文本中中文字的词频：
def stats_text_cn(text,count):  
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    
    text1 = []
    for i in text:  # 这个循环有效，说明一串汉字也是一个字符串，每个汉字就是其中的一个元素，可以用for in 来遍历，其中i代表了每个汉字的unicode编码
        if i < u'\u4e00' and i > u'\u9fff':     # 挑选出非中文字
            text=text.split(i,"") # 将非中文字符替换
    seg_list = jieba.cut(text,cut_all =False) 
    
    for j in seg_list:
             if len(j) >= 2 : #只统计长度大于等于2的词
              text1.append(j)
    text1 = collections.Counter(text1).most_common(count)  #按出现次数从大到小排列
    return text1

with open('tang300.json','r',encoding='UTF-8') as f:
    a = f.read()
try:
    if not isinstance(a,str):
        raise ValueError()
    
except ValueError:
    print('输入的不是文本格式')  
print(stats_text-cn(a,10))