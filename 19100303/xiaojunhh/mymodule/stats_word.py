

# 示例字符串
string1 =  '''
愚公移山
太行，王屋二山的北面，住了一個九十歲的老翁，名叫愚公。二山佔地廣闊，
擋住去路，使他和家人往來極為不便。
一天，愚公召集家人說：「讓我們各盡其力，剷平二山，開條道路，直通豫州，
你們認為怎樣？」
大家都異口同聲贊成，只有他的妻子表示懷疑，並說：「你連開鑿一個小丘的
力量都沒有，怎可能剷平太行、王屋二山呢？況且，鑿出的土石又丟到哪裏去
呢？」
大家都熱烈地說：「把土石丟進渤海裏。」
於是愚公就和兒孫，一起開挖土，把土石搬運到渤海去。
愚公的鄰居是個寡婦，有個兒子八歲也興致勃勃地走來幫忙。
寒來暑往，他們要一年才能往返渤海一次。
住在黃河河畔的智叟，看見他們這樣辛苦，取笑愚公說：「你不是很愚蠢嗎？
你已一把年紀了，就是用盡你的氣力，也不能挖去山的一角呢？」
愚公歎息道：「你有這樣的成見，是不會明白的。你比那寡婦的小兒子還不如
呢！就算我死了，還有我的兒子，我的孫子，我的曾孫子，他們一直傳下去。
而這二山是不會加大的，總有一天，我們會把它們剷平。」
智叟聽了，無話可說：
二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精
神，就命兩位大力神揹走二山。
HowTheFoolishOldManMovedMountains
Yugongwasaninety-year-oldmanwholivedatthenorthoftwo
highmountains,MountTaixingandMountWangwu.
Stretchingoverawideexpanseofland,themountainsblocked
yugong’swaymakingitinconvenientforhimandhisfamilyto
getaround.
Onedayyugonggatheredhisfamilytogetherandsaid,”Let’sdo
ourbesttolevelthesetwomountains.Weshallopenaroad
thatleadstoYuzhou.Whatdoyouthink?”
Allbuthiswifeagreedwithhim.
“Youdon’thavethestrengthtocutevenasmallmound,”
mutteredhiswife.“Howonearthdoyousupposeyoucanlevel
MountTaixinandMountWanwu?Moreover,wherewillallthe
earthandrubblego?”
“DumpthemintotheSeaofBohai!”saideveryone.
SoYugong,hissons,andhisgrandsonsstartedtobreakup
rocksandremovetheearth.Theytransportedtheearthand
rubbletotheSeaofBohai.
NowYugong’sneighbourwasawidowwhohadanonlychildeight
yearsold.Eveningtheyoungboyofferedhishelpeagerly.
Summerwentbyandwintercame.IttookYugongandhiscrewa
fullyeartotravelbackandforthonce.
OnthebankoftheYellowRiverdwelledanoldmanmuch
respectedforhiswisdom.Whenhesawtheirback-breaking
labour,heridiculedYugongsaying,”Aren’tyoufoolish,my
friend?Youareveryoldnow,andwithwhateverremainsofyour
waningstrength,youwon’tbeabletoremoveevenacornerof
themountain.”
Yugongutteredasighandsaid,”Abiasedpersonlikeyouwill
neverunderstand.Youcan’tevencomparewiththewidow’s
littleboy!”
“EvenifIweredead,therewillstillbemychildren,my
grandchildren,mygreatgrandchildren,mygreatgreat
grandchildren.Theydescendantswillgoonforever.Butthese
mountainswillnotgrowanytaler.Weshalllevelthemoneday!”
hedeclaredwithconfidence.
Thewiseoldmanwastotallysilenced.
Whentheguardiangodsofthemountainssawhowdetermined
Yugongandhiscrewwere,theywerestruckwithfearand
reportedtheincidenttotheEmperorofHeavens.
FilledwithadmirationforYugong,theEmperorofHeavens
orderedtwomightygodstocarrythemountainsaway.
'''

import collections
import re

def stats_text_en(string_en):
    ''' 统计英文词频
    
    第一步：过滤英文字符，并将string拆分为list。
    第二步：清理*-等标点符号。
    第三步：使用collections库中的Counter函数进行词频统计并输出统计结果。
    '''
    print("处理前的原始字符串\n\n",string_en)
    result = re.sub("[^A-Za-z]", " ", string_en.strip())#把非A-Z和a-z的字符串全部去除掉
    print("处理后的结果\n\n",result)
    newList = result.split( )
    i=0
    for i in range(0,len(newList)):
        newList[i]=newList[i].strip('*-,.?!')
        if newList[i]==' ': 
            newList[i].remove(' ')
        else:
            i=i+1
    print('英文单词词频统计结果： ',collections.Counter(newList),'\n')


def stats_text_cn(string_cn):
    ''' 统计中文汉字字频
    
    第一步：过滤汉字字符，并定义频率统计函数 stats()。
    第二步：清除文本中的标点字符,将非标点字符组成新列表 new_list。
    第三步：遍历列表，将字符同上一次循环中频率统计结果作为形参传给统计函数stats()。
    第四步：统计函数在上一次统计结果基础上得出本次统计结果，赋值给newDict。
    第五步：new_list遍历结束，输出倒序排列的统计结果。
    '''
    result1 = re.findall(u'[\u4e00-\u9fff]+', string_cn)
    newString = ''.join(result1)

    def stats(orgString, newDict) :
        d = newDict
        for m in orgString :
            d[m] = d.get(m, 0) + 1
        return d
    
    new_list = []
    for char in newString :
        cn = char.strip('-*、。，：？！……')
        new_list.append(cn)
    
    words = dict()
    for n in range(0,len(new_list)) :
        words = stats(new_list[n],words)
    newWords = sorted(words.items(), key=lambda item: item[1], reverse=True) 
    print('中文汉字字频统计结果： ',dict(newWords))

# 调用函数
stats_text_en(string1)
# stats_text_cn(string1)

# stats_text 函数，实现调用stats_text_en , stats_text_cn ，输出合并词频统计结果
import collections
import re


def stats_text1_en(en) :
    ''' 英文词频统计'''
    text_en = re.sub("[^A-Za-z]", " ", en.strip())
    enList = text_en.split( )
    return collections.Counter(enList)

        
def stats_text1_cn(cn) :
    ''' 汉字字频统计 '''
    cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
    cnString = ''.join(cnList)
    return collections.Counter(cnString)

def stats_text(text_en_cn) :
    ''' 合并英汉词频统计 '''
    return (stats_text_en(text_en_cn)+stats_text_cn(text_en_cn))


