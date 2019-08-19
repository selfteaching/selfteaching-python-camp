# 统计参数中每个英文单词出现的次数
def stats_text_en(text):
    elements = text.split()
    words = []
    symbols = ',.*_!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        if len(element):
            words.append(element)
    counter = {}
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)
    # 函数返回值用 return 进行返回，如果没有 return 返回值则为 None
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)


# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    cn_characters = []
    for character in text:
        # unicode 中 中文 字符的范围
        if '\u4e00' <=  character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)


en_text = '''
Goodbye Again, Cambridge


Goodbye Again, Cambridge!

I leave softly, gently,

Exactly as I came.I wave to the western sky,Telling it goodbye softly, gently.

The golden willow at the river edge

Is the setting sun‘s bride.Her quivering reflectionStays fixed in my mind.

Green grass on the bank

Dances on a watery floorIn bright reflection.I wish myself a bit of waterweedVibrating to the ripple.Of the River Cam.

That creek in the shade of the great elms

Is not a creek but a shattered rainbow,Printed on the waterAnd inlaid with duckweed,It is my lost dream.

Hunting a dream?

Wielding a long punting poleI get my boat into green water,Into still greener grass.In a flood of starlightOn a river of silver and diamondI sing to my heart‘s content.

But now, no, I cannot sing

With farewell in my heart.Farewells must be quiet, mute,Even the summer insects are silent,Knowing I am leaving.The Cambridge night is soundless.

I leave quietly

As I came quietly.I am leavingWithout taking so muchAs absp; piece of cloud.But with a quick jerk of my sleaveI wave goodbye.
'''

cn_text = '''
 再别康桥


 轻轻的我走了，
 正如我轻轻的来；
 我轻轻的招手，
 作别西天的云彩。
 　
 那河畔的金柳，
 是夕阳中的新娘；
 波光里的艳影，
 在我的心头荡漾。
 　
 软泥上的青荇，
 油油的在水底招摇；
 在康河的柔波里，
 我甘心做一条水草！
 　
 那榆荫下的一潭，
 不是清泉，
 是天上虹；
 揉碎在浮藻间，
 沉淀着彩虹似的梦。
 　
 寻梦？撑一支长篙，
 向青草更青处漫溯；
 满载一船星辉，
 在星辉斑斓里放歌。
 　
 但我不能放歌，
 悄悄是别离的笙箫；
 夏虫也为我沉默，
 沉默是今晚的康桥！
 　
 悄悄的我走了，
 正如我悄悄的来；
 我挥一挥衣袖，
 不带走一片云彩。
'''

# 搜索__name__ == __main__
# 一般情况下在文件内 测试 代码的时候以下面的形式进行
if __name__ == '__main__':
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数 ==>\n', en_result)
    print('统计参数中每个中文汉字出现的次数 ==>\n', cn_result)