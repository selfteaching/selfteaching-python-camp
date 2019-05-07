def stats_text_en(text):
    """
    接收一个 text ，统计其中的英文单词出现的次数
    以下字符不计入统计：
    '!"#$%&()*+,-./:;<=>?@[]\^_`{|}~'
    """
    a = {}

    b = ''.join(i for i in text if i not in """!"#$%&()*+,-./:;<=>?@[]\^_`{|}~""")

    for word in b.split():
        if word not in a:
            a[word] = 1
        else:
            a[word] += 1
   
    c = sorted(a.items(),key=lambda x:x[1],reverse=True)
    return c

def stats_text_cn(text):
    """
    接收一个 text ，统计其中的英文单词出现的次数
    以下字符不计入统计：
    '空格、换行、0123456789!"#$%&()*+,-./:;<=>?@[]\^_`{|}~，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥…'
    """

    a = {}
    
    b = ''.join(i for i in text if i not in """\n\u30000123456789!"#$%&()*+,-./:;<=>?@[]\^_`{|}~，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥…""")

    for word in b:
        if word not in a:
            a[word] = 1
        else:
            a[word] += 1
   
    c = sorted(a.items(),key=lambda x:x[1],reverse=True)
    return c

texten="""
Retrieve a given field value. The key argument will be either an integer or a string. If it is an integer, it represents the index of the positional argument in args; if it is a string, then it represents a named argument in kwargs.

The args parameter is set to the list of positional arguments to vformat(), and the kwargs parameter is set to the dictionary of keyword arguments.

For compound field names, these functions are only called for the first component of the field name; Subsequent components are handled through normal attribute and indexing operations.

So for example, the field expression ‘0.name’ would cause get_value() to be called with a key argument of 0. The name attribute will be looked up after get_value() returns by calling the built-in getattr() function.

If the index or keyword refers to an item that does not exist, then an IndexError or KeyError should be raised.
"""
textcn="""
只要具备这5个特点，一篇文章才是好作文，建议学生家长收藏！

说到作文，不仅仅是学生头痛欲裂，而且连学生家长和老师也相当头疼。因为在我们身边，真正文章写得特别好的人虽然也有，但极其稀少。写一篇文章不难，但要写一篇好的作文就不是那么简单了。那么，什么样的作文才是好作文呢？


我觉得，只要具备以下这5个特点，一篇文章才是名副其实的好作文：

首先，语言要真实。

真实是作文的生命线。一篇胡编滥造的文章，毫无真实性可言，写出来的东西自己都不信，那么就算那篇文章语句再优美也会给人产生一种严重不适的感觉。只有建立在真实的基础上，文章才能打动自己，感动别人。


有的小学生在写作的时候，总喜欢把家长的手机拿过来进行“百度”一番，结果搬过来的文章连标点符号都不是自己的……这样“写”作文，到底有什么意义？文如其人，一个人的文章可以存在瑕疵，但绝不能失真、失实、失信。小学生的作文只有做到“我笔写我心”，才能在今后的写作道路上行稳致远。


其次，字迹要端庄。

作文的字迹漂亮、整洁，总会给人一种眼前一亮的感觉。每一笔每一划都“精雕细刻”，每一个字都如同艺术品，那么在作文质量差不多的情况下，字迹端庄的作文得到的分数十有八九会高好多分。退一万步讲，就算字写得不是那么漂亮，但每一个字都很认真地写，那么就凭这股认真的态度，也会给评卷的老师留下相当好的印象。


第三，语句要流畅。

语句是否流畅，表达是否清晰，是判断一篇文章是否优秀的一大因素。语言简洁明了，没有太多别扭的语句；文章词汇量丰富，用词极其精准，不存在佶屈聱牙的句子，是一篇好作文最基本的需求。


第四，立意要深刻。

很多时候，作文能否得高分，在很大程度上取决于文章的立意有多高。古人有云：“意，犹帅也”，说的是立意相当于一篇文章的灵魂所在。一篇立足于真实性，又立意深刻高远的文章，在考场作文中不想拿高分都难。


第五，构思要新颖。

很多小学生写作文，一写到感动就肯定是“妈妈把39.5度高烧的我冒雨送到医院，然后她自己全身淋湿”；一写到助人为乐就肯定是扶老奶奶过马路，最后结尾总是“这是我应该做的事情”……这样的文章一篇两篇情有可原，但全班同学千篇一律就让评卷的老师味同嚼蜡。


建一座房子，就要把房屋的空架结构搞定。一篇文章的构思如果相当新颖的话，可读性就要高出很多。从不同的角度去写同一个题目的文章，用别出心裁的构思赢得读者的青睐，我觉得对于初学写作的小学生而言是有百利而无一害的。


你觉得好作文还有哪些特点呢？欢迎在评论区留言探讨。

"""
print(stats_text_en(texten))
print(stats_text_cn(textcn))