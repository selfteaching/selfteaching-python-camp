text ='''
The invariants still hold: pivot >= all in [lo, left) and
* pivot < all in [left, start), so pivot belongs at left. Note
* that if there are elements equal to pivot, left points to the
* first slot after them -- that's why this sort is stable.
* Slide elements over to make room for pivot.
'''

'''
统计参数text中每个英⽂文单词出现的次数，最后返回⼀个按词频降序排列列的数组
'''
def stats_text_en(text):
    word_freq = {}
    text = str(text).split()
    words = []
    #把单词从字符串里选出来
    symbols = ",.*-!"
    for item in text:
        word = ''
        for letter in symbols:
            item = item.replace(letter,'')
        if len(item):    
            words.append(item)
    words_list = set(words)    
    # 计算每一个单词出现的次数并排序
    for item in words_list:
        word_freq[item] = words.count(item)
    return sorted(word_freq.items(),key = lambda x:x[1],reverse = True)
# print(stats_text_en(text))


# 接受⼀一 个字符串text 作为参数,实现该函数的功能:统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的 数组

textfile = '''1. 创建⼀一个名为 1001S02E06_stats_word.py 的⽂文件
2. 定义⼀一个名为 stats_text_en 的函数，函数接受⼀一个字符串串 text 作为参数
3. 实现该函数的功能(同day5任务2):统计参数中每个英⽂文单词出现的次数，最后返回⼀一
个按词频降序排列列的数组
4. 为 stats_text_en 添加注释说明
'''

#汉字和单词不同的地方在于汉字都是单字符的，所以只需要判断一个单个字符就可以了
def character_text_cn(text):
    character_freq = {}
    characters = []
    #把单词从字符串里选出来
    for character in text:
        if u'\u4e00' <= character <= u'\u9fff':
            characters.append(character)
    character_set = set(characters)

    for character in character_set:
        character_freq[character] = characters.count(character)
    return sorted(character_freq.items(),key = lambda x:x[1],reverse = True)  

print(character_text_cn(textfile))