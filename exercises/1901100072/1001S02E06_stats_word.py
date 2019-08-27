text = '''When I do count the clock that tells the time,And see the brave day sunk in hideous night;When I behold the violet past prime,And sable curls all silver'd o'er with white:When lofty trees I see barren of leaves,Which erst from heat did canopy the herd,And summer's green, all girded up in sheaves,Born on the bier with white and bristly beard;Then of thy beauty do I question make,
That thou among the wastes of time must go,Since sweets and beauties do themselves forsake,And die as fast as they see others grow;And nothing 'gainst Time's scythe can make defence.Save breed, to brave him when he takes thee hence.
. '''
def stats_text_en(text):  # 统计英文词频
    a = text.split()        #把字符串变成列表
    import collections        #统计函数
    b=collections.Counter(a)
    return (b)                 #回旋值，重复定义的
print('英文单词出现的次数==>',stats_text_en(text))
      



text2 = '''Building stuffs——做出东西来。我个人最看中人的这个特质。人群中只有少数人最终能拿出完整的作品——人与人之间的差异是如此之大，乃至于少数人有作品，更少数人有好的作品，只极少数极少数人才可能作出传世的作品；而与此同时，绝大多数人（万分之九千九百九十九的人）一辈子都没有像样的作品，他们连一篇作文都写不明白。
从一开始就要想尽一切办法做出完整的作品来，哪怕最初的作品很差——但必须完整。那些有完整作品的人，能力、耐力、学习能力都会超出他人许多倍。无论看起来多简单的作品，只要是完整的，其表面之下的复杂程度是那些没做出过东西的人全然无法想像的。
我甚至经常建议我的合伙人们，在招人的时候，把这一点当作最靠谱的判断方式。少废话，少吹牛逼，给我看看你的作品。这个原则可以一下子过滤掉所有的废物。
另外一个很自然的现象是，如果一个人能做出像样的东西来，那么他身边的聪明人密度无论如何都会比其他人的高出很多。 '''
def stats_text_cn(text2):  # 统计中文词频
    countcn={}
    for ch in text2:
        if u'\u4e00' <= ch <= u'\u9fff':
            countcn[ch] = text2.count(ch)
    countcn = sorted(countcn.items(), key=lambda item: item[1], reverse=True)  #按出现数字从大到小排列
    return countcn
print(stats_text_cn(text2))

