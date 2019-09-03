text1 = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly. 
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense. 
'''

def stats_text_en(text1):   #以降序方式统计英文词频
    elements = text1.split()
    words = []
    symbols = ',.'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element):
            words.append(element)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)
if __name__ == '__main__':
    en_result = stats_text_en(text1)
    print('英文单词词频降序排列 \n', en_result)

text2 = '''
很多时候，我们在重组自己的偏见时，还以为自己是在思考；
在重复以往的错误时，还以为是在坚持梦想；
在消极荒废时，还以为是在放松；
在伤害别人自尊时，还以为是直率；
在故步自封时，还以为是在坚守；
在随便放弃时，还以为是在选择；
在喝得酩酊大醉时，还以为是豪爽；
在不思进取时，还以为是低调。
'''

def stats_text_cn(text2):  #以降序方式统计中文词频
    cn_character = []
    for character in text2:
        if'\u4e00'<=character<='\u9fff':
            cn_character.append(character)
    counter={}
    cn_character_set = set(cn_character)
    for character in cn_character_set:
        counter[character] = cn_character.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

if __name__ == '__main__':
    cn_result = stats_text_cn(text2)
    print('中文汉字词频降序排列 \n',cn_result)
