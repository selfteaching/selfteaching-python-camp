#用函数做词频统计

#英文文章

count_text1 ='''The US media reports suggest Robert Mueller's inquiry has taken the first step towards possible criminal charges.
According to Reuters news agency, the jury has issued subpoenas over a June 2016 meeting between President Donald Trump's son and a Russian lawyer.
The president has poured scorn on any suggestion his team colluded with the Kremlin to beat Hillary Clinton.
In the US, grand juries are set up to consider whether evidence in any case is strong enough to issue indictments for a criminal trial. They do not decide the innocence or guilt of a potential defendant.
The panel of ordinary citizens also allows a prosecutor to issue subpoenas, a legal writ, to obtain documents or compel witness testimony under oath.
Trump: US-Russia relations are at 'dangerous low'
The Trump-Russia saga in 200 words
Russia: The 'cloud' over the White House
Now it's deadly serious
Anthony Zurcher, BBC North America reporter
Robert Mueller's special counsel investigation has always been a concern for the Trump administration. Now it's deadly serious business.
With the news that a grand jury has been convened in Washington DC, and that it is looking into the June 2016 meeting between Donald Trump Jr and Russian nationals, it's clear the investigation is focusing on the president's inner circle.
This news shouldn't come as a huge shock, given that Mr Mueller has been staffing up with veteran criminal prosecutors and investigators. It is, however, a necessary step that could eventually lead to criminal indictments. At the very least it's a sign that Mr Mueller could be on the trail of something big - expanding the scope beyond former National Security Adviser Michael Flynn and his questionable lobbying. It also indicates his investigation is not going to go away anytime soon.
In the past, when big news about the Russia investigation has been revealed, Mr Trump has escalated his rhetoric and taken dead aim at his perceived adversaries. The pressure is being applied to the president. How will he respond?
At a rally in Huntington, West Virginia, on Thursday evening, Mr Trump said the allegations were a "hoax" that were "demeaning to our country".
"The Russia story is a total fabrication," he said. "It's just an excuse for the greatest loss in the history of American politics, that's all it is."
The crowd went wild as he continued: "What the prosecutor should be looking at are Hillary Clinton's 33,000 deleted emails."
"Most people know there were no Russians in our campaign," he added. "There never were. We didn't win because of Russia, we won because of you, that I can tell you."
Mr Trump's high-powered legal team fielding questions on the Russia inquiry said there was no reason to believe the president himself is under investigation.
Ty Cobb, a lawyer appointed last month as White House special counsel, said in a statement: "The White House favours anything that accelerates the conclusion of his work fairly.
"The White House is committed to fully co-operating with Mr Mueller."
Earlier on Thursday, the US Senate introduced two separate cross-party bills designed to limit the Trump administration's ability to fire Mr Mueller.
The measures were submitted amid concern the president might dismiss Mr Mueller, as he fired former FBI director James Comey in May, citing the Russia inquiry in his decision.
'''

#英文词频排序
def stats_text_en(text1):
    # 把字符串去掉转行、大写换小写、去掉单词两边字符
#    for f in ', . \ : ; "':#未成功，尝试寻找更好的方式中
#        text = text1.replace(f,'').lower().split(' ')

    text = text1.replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').lower().split(' ')

    #创建一个字典
    count = {}
    # 如果字典里有该单词则词频+1，否则添加入字典
    for word in text:
        if word in count.keys():
            count[word] = count[word] + 1
        else:
            count[word] = 1
    #按照词频从高到低排列
    count_list=sorted(count.items(),key=lambda a:a[1],reverse=True)
    return count_list
print ("单词出现频率排列如下：",stats_text_en(count_text1))


#中文文章
count_text2 ='''在东胜神州傲来国海滨的花果山顶有一块仙石。一日，仙石轰然迸裂，惊天动地，化出了一个石猴。这石猴灵敏聪慧，他交结群猴，在水帘洞找到安家的好所在。群猴尊石猴为美猴王。美猴王为寻找长生不老的仙方，独自驾筏，漂洋过海，来到一所渔村。

他拾得衣衫，偷来鞋帽，并去饭馆饮酒吃面，闹了许多笑话，也学了几分人样。猴王一路寻访，终于登上灵台方寸上，在斜月三星洞拜见了菩提祖师。

祖师为他取名孙悟空。从此悟空参禅悟道，学习武艺，掌握了七十二般变化的本领。花果山上，群猴却面临危难。悟空驾云回来，与混世魔王展开了一场厮杀。

美猴王战胜了混世魔王，花果山上喜气洋洋，小猴们每日操演武艺，十分快乐。悟空闯入东海龙宫，向龙王索取镇海神针——如意金箍棒。这棒虽重一万三千五百斤，却大可撑天着地，小可变针，藏入耳内。

悟空酒醉睡去，忽见两个阴差前来索命，悟空大闹阎罗殿，命判官取出生死簿，一笔勾去了猴类的生年死月。龙王、阎王上玉帝处告状，玉帝派太白金星下界招抚猴王，请他上天作官。悟空欣然前往，在武曲星君的捉弄下，玉帝封他做了弼马温。

当悟空明白了自己不过是个马夫后，大怒之下回转花果山，扯起大旗，自称齐天大圣。玉帝不能容忍，叫托塔天王与哪吒率领天兵神将，杀向花果山。
'''

#中文字频排序
def stats_text_cn(text2):

#    for f in ',.-\n ':#该语句未成功,寻找更好的解决办法中
#        text = text2.replace(f,'')
#去掉符号    
    text = text2.replace('—','').replace(' ','').replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','')
#建立字典
    count = {}
#用for循环做字频统计    
    for word in text:
        if word in count.keys():
            count[word] = count[word] + 1
        else:
            count[word]=1
#调整排序并输出
    count_list = sorted(count.items(),key=lambda a:a[1],reverse=True)
    return count_list
#输出
print ("字出现频率排列如下：",stats_text_cn(count_text2))