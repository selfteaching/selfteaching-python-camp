text = '''
ઊل఼

ॡᤈ҅ሴ੻ԫઊጱ۹ᶎ҅֘ԧӞ㮆Ԝ܈䵇ጱᘌᗷ҅ݞݷ఼لԫ̶ઊ㬟ࣈ䔃橃҅䢘݄֘᪠ֵ҅՜
̶׎ਹՈஃ㬵䮩傶ӧ޾
Ӟॠ఼҅ݟلᵞਹՈ抋ғ̿捰౯㮉ݱ哴ٌێ҅㴗ଘԫઊ҅樄䬈᭲᪠҅ፗ᭗ᨠ૞֦҅㮉扯傶ெ
䰬Ҙ̀
य़ਹ᮷吖ݶݗ宙摁౮҅ݝํ՜ጱঠৼᤒᐏ䛸ወ҅㪔抋ғ֦̿昧樄槓Ӟ㮆ੜӯጱێᰁ᮷䷱ํ҅ெ
ݢᚆ㴗ଘॡᤈ̵ሴ੻ԫઊޫҘ丆Ӭ҅槓ڊጱࢿᎪ݈㪐ߺک惾݄ޫҘ̀
य़ਹ᮷公ᅱࣈ抋ғ̿಩ࢿᎪ㪐昲Ⴣၹ惾̶̀
ෝฎ఼ل੪޾㱾䋂҅Ӟ᩸樄೵ࢿ಩҅ࢿᎪ൪晁کჃၹ̶݄
఼لጱ曓੷ฎ㮆ੋ䇹҅ํ㮆㱾ৼك䵇Ԟ岉ᛘۡۡࣈᩳ㬵䒻஬̶
੆㬵าஃ҅՜㮉ᥝӞଙ಍ᚆஃᬬჃၹӞ̶ེ
֘ࣁ焗မမ኷ጱฬݕ҅፡憎՜㮉春䰬ᬔᝒ҅ݐᒞ఼ل抋ғ֦̿ӧฎஉ఼ᤁ㻟Ҙ֦૪Ӟ಩ଙ夵
ԧ҅੪ฎአ哴֦ጱ䶷ێ҅Ԟӧᚆ೵݄ઊጱӞ᥯ޫҘ̀
఼ل䴫௳᭲ғ֦̿ํ春䰬ጱ౮憎҅ฎӧ䨝กጮጱ̶֦ྲᮎੋ䇹ጱੜ㱾ৼ晤ӧইޫѺ੪ᓒ౯ྒ
ԧ҅晤ํ౯ጱ㱾ৼ҅౯ጱ䋂ৼ҅౯ጱ้䋂ৼ҅՜㮉Ӟፗ㯽ӥ̶݄ᘒ春ԫઊฎӧ䨝ےय़ጱ҅婦ํ
Ӟॠ҅౯㮉䨝಩ਙ㮉㴗ଘ̶̀
ฬݕ室ԧ҅僻扖ݢ抋ғ
ԫઊጱਝ捔ᐟᤩ఼لጱ䁎ྫྷᔜᐟ㽔ׯ҅׎ॵԪྌ಩Ꭳॠଂ̶ॠଂ֫๐఼لጱᔜᐟ҅੪޸㲍֖य़
ێᐟ䠈ᩳԫઊ̶
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high
mountains, Mount Taixing and Mount Wangwu.

Stretching over a wide expanse of land, the mountains blocked
yugong’s way making it inconvenient for him and his family to get
around.
One day yugong gathered his family together and said,”Let’s do our
best to level these two mountains. We shall open a road that leads to
Yuzhou. What do you think?”
All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered his
wife. “How on earth do you suppose you can level Mount Taixin and
Mount Wanwu? Moreover, where will all the earth and rubble go?”
“Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and
remove the earth. They transported the earth and rubble to the Sea of
Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years
old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full
year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected for
his wisdom. When he saw their back-breaking labour, he ridiculed
Yugong saying,”Aren’t you foolish, my friend? You are very old now,
and with whatever remains of your waning strength, you won’t be able
to remove even a corner of the mountain.”
Yugong uttered a sigh and said,”A biased person like you will never
understand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, my
grandchildren, my great grandchildren, my great great grandchildren.
They descendants will go on forever. But these mountains will not
grow any taler. We shall level them one day!” he declared with
confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong and
his crew were, they were struck with fear and reported the incident
to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens ordered two
mighty gods to carry the mountains away.
'''

#定义一个名字为stats_text_en的函数，功能为统计出现单词的个数
def stats_text_en(strText):
    #创建一个空字典用来统计单词个数
    dic={}
    #将文本中的非单词因素去掉
    text2=strText.replace("\n","").replace("."," ").replace("!","").replace("--","").replace("  "," ")
    #将文本按照一个空格切割
    list1=text2.split(" ")

    #遍历切割的列表
    for l1 in list1:
        #判断该字符串是否由字母组成
        if l1.isalpha():
            #如果单词不在dic字典中，则设置为0
            count=dic.get(l1,0)
            count+=1
            dic[l1]=count
    #将dic转为dic.items()，根据单词出现个数排序，降序
    list2=sorted(dic.items(),key=lambda item:item[1],reverse=True)
    return list2

#封装统计中文汉字字频的函数
def stats_text_cn(textC):
    dic={}
    for ch in textC:
        #判断该字符是否是中文
        if ch>="\u4e00" and ch<="\u9fff":
            count=dic.get(ch,0)
            dic[ch]=count+1
    
    list3=sorted(dic.items(),key=lambda item:item[1],reverse=True)        
    return list3

#将统计中文词频和英文词频的函数封装为一个模块
def stats_text(text):
    textC=stats_text_cn(text)
    print(textC)

    print(stats_text_en(text))

stats_text(text)



