dictionary = {}
dic_3 = {}
dic_4 = {}
text = str
# 统计参数中每个英文单词出现的次数，最后返还一个按词频降序排列的数组
def stats_text_en(text):
    text=text.replace(',',' ').replace('.',' ').replace('*',' ').replace('--',' ')
    text1=text.split()
    for i in text1:
        dictionary.update({i:text1.count(i)})#通过key:计数函数来更新字典
    return dictionary
dictionary1=sorted(dictionary.items(),key=lambda x:x[1],reverse=True)#sorted()排序;.items()遍历字典(键,值) 元组,

print("统计英文词频的结果为:")
print(dictionary1)#打印统计英文词频的结果

#统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组
cndict = {}#定义一个空字典
def stats_text_cn(text):
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff': #判断一个unicode是否是汉字
            cndict[i] = text.count(i)
    return cndict
cndict1=sorted(cndict.items(),key=lambda item:item[1],reverse = True)#为了阅读方便，检索完毕后对字典进行按值从大到小排序                          

print("统计中文词频的结果为:")
print(cndict1)#打印统计中文词频的结果
        
# 合并英汉词频统计 
def stats_text(text):
    dic_1 = stats_text_cn(text) # 调用函数1统计中文字词频
    if not isinstance(text,str):
            raise ValueError('输入的不是文本格式，请重新输入：') 
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':
            text = text.replace(i,"") #删除所有中文字
            text = text.replace('「', '').replace('」', '').replace('，', '').replace('。', '').replace('：', '').replace('？', '').replace('！', '')
        # 以上一句删除所有中文标点
    dic_2 = stats_text_en(text) # 调用2函数统计英文单词词频
    dic_3.update(dic_2)
    dic_3.update(dic_1) # 将之前分别得到的两个中英文词频结果字典合并
    dic_4=sorted(dic_3.items(),key = lambda x:x[1],reverse = True) # 对合并后的字典进行排序，得出混合排序结果
print(dic_4)
