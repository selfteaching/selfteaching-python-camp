text = '''When I do count the clock that tells the time,And see the brave day sunk in hideous night;When I behold the violet past prime,And sable curls all silver'd o'er with white:When lofty trees I see barren of leaves,Which erst from heat did canopy the herd,And summer's green, all girded up in sheaves,Born on the bier with white and bristly beard;Then of thy beauty do I question make,
That thou among the wastes of time must go,Since sweets and beauties do themselves forsake,And die as fast as they see others grow;And nothing 'gainst Time's scythe can make defence.Save breed, to brave him when he takes thee hence.
. '''

#先将字符串分割成list
stats_text_en = text.split()
#定义一个新的list变量，存储过处理的单词
words = []
#剔除非单词符号，
symbols = ', . * - !'
for element in stats_text_en:
    for symbol in symbols:
        element = element.replace(symbol,'')
    if len(element):
       words.append(element)

counter ={}
word_set = set(words)
for word in word_set:
    counter[word] =words.count(word)
print('英文单词出现的次数==>',counter)
      
print('从大到小输出所有的单词及出现的次数==>',sorted(counter.items(),key=lambda x:x[1],reverse=True))


text = '''Building stuffs——做出东西来。我个人最看中人的这个特质。人群中只有少数人最终能拿出完整的作品——人与人之间的差异是如此之大，乃至于少数人有作品，更少数人有好的作品，只极少数极少数人才可能作出传世的作品；而与此同时，绝大多数人（万分之九千九百九十九的人）一辈子都没有像样的作品，他们连一篇作文都写不明白。
从一开始就要想尽一切办法做出完整的作品来，哪怕最初的作品很差——但必须完整。那些有完整作品的人，能力、耐力、学习能力都会超出他人许多倍。无论看起来多简单的作品，只要是完整的，其表面之下的复杂程度是那些没做出过东西的人全然无法想像的。
我甚至经常建议我的合伙人们，在招人的时候，把这一点当作最靠谱的判断方式。少废话，少吹牛逼，给我看看你的作品。这个原则可以一下子过滤掉所有的废物。
另外一个很自然的现象是，如果一个人能做出像样的东西来，那么他身边的聪明人密度无论如何都会比其他人的高出很多。 '''
stats_text_cn = text.split()##先将字符串分割成list
word_lst = []#定义一个新的list变量，存储过处理的单词
word_dict = {}
exclude_str = "，。！？、（）【】<>《》=：+-*—“”…" #剔除非汉字符号，
for line in stats_text_cn: # 用字典统计每个字出现的个数 
    for char in line:
        word_lst.append(char)
for char in word_lst:# strip去除各种空白
    if char not in exclude_str:
        if char.strip() not in word_dict:
            word_dict[char] = 1
        else:
            word_dict[char] += 1
lstWords = sorted(word_dict.items(), key=lambda x:x[1],  reverse=True) #x[1]是按字频排序，x[0]则是按字排序
print('从大到小输出所有的汉字及出现的次数==>',sorted(word_dict.items(),key=lambda x:x[1],reverse=True))

