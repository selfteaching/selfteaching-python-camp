text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly. 
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!
'''

#统计参数中出现的英文单词出现的次数
def stats_text_en(text):#定义统计英文单词词频函数stats_text_en(text1)
    elements = text.split()#参数分割成单个元素，清理成单个单词
    words = [] #存放单词列表
    symbols = ',.*-!?"' #过滤符号
    for element in elements:#遍历元素列表，清理非英文符号
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element): #辨别单词长度是否大于0
            words.append(element)#真正单词列入words列表
    counter = {} #定义字典，存放词频
    word_set = set(words) #剔除遍历重复
    for word in word_set:
        counter[word] = words.count(word) 
    return sorted(counter.items(), key=lambda x:x[1],reverse=True)#返回
if __name__ == '__main__':#搜索__name__ == '__main__，测试代码
    en_result = stats_text_en(text)
    print('英文单词词频降序排列 \n', en_result)
 

#2.封装统计中文汉字字频的函数
text = '''《稀缺》
在稀缺状态下,我们会产生管窥心态。
当稀缺成为带宽负担时,我们会对当下更加关注,从而导致我们产生借用行为。
而当我们借用时,就是给自己的将来挖下了更深的坑。
今天的稀缺,将造成明天更大的稀缺。
当我们为了解决眼下的难题而极度专注时,就无法有效地规划未来,这样一来,向前看的能力就很可能会因管窥负担而丧失'''

def stats_text_cn(text):#定义函数
    cn_character = []
    for character in text:
         if'\u4e00'<=character<='\u9fff': #unicode 中文字符范围
             cn_character.append(character)
    counter={}
    cn_character_set = set(cn_character)#字符定义成集合
    for character in cn_character_set:#遍历集合
        counter[character] = cn_character.count(character)#统计字数并附给
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)#排序


if __name__ == '__main__':
    cn_result = stats_text_cn(text)
    print('中文汉字字频降序排列 \n', cn_result)

 #合并英文词频和中文词频结果
def stats_text(text):
    return stats_text_cn(text) + stats_text_en(text)

