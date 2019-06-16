#统计参数中每个英文单词出现的次数
def stats_text_en(text):
    elements=text.split()
    words=[]
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len (element) and element.isascii():
            words.append(element)
    counter={}
    word_set =set(words)

    for word in word_set:
        counter[word]=words.count(word)
#函数返回值用return 进行返回，如果没有return 返回值则为 None    
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)
#统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
   cn_characters=[]
   for character in text:
       #unicode中 中文字符的范围
       if'\u4e00'<=character<='\u9fff':
          cn_characters.append(character)
   counter={}
   cn_character_set=set(cn_characters) 
   for character in cn_character_set:
       counter[character]=cn_characters.count(character)
   return sorted (counter.items(),key=lambda x:x[1],reverse=True)

def stats_text(text):
    '''
    合并 英文词频 和 中文词频 的结果
    '''
    return stats_text_en(text)+stats_text_cn(text)


#搜索__name__==__main__
#一般情况下在文件内 测试 代码的时候以下面的形式进行
if __name__=='__main__':
    en_text='''
The Zen of Python,by Tim Peters
'''