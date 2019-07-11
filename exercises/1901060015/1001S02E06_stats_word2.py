text="""村上春树，日本后现代主义作家，1949年1月12日生于京都伏见区。毕业于早稻田大学第一文学部演剧科。
村上春树29岁开始写作，第一部作品《且听风吟》即获得日本群像新人奖，1987年第五部长篇小说《挪威的森林》上市至2010年在日本畅销一千万册，国内简体版到2004年销售总量786万，引起“村上现象”。
其作品在世界范围内具有广泛知名度，作品风格深受欧美作家的影响，基调轻盈，少有日本战后阴郁沉重的文字气息，被称作第一个纯正的“二战后时期作家”，并被誉为日本80年代的文学旗手。 [1]  
2017年2月24日，村上春树出版两卷本长篇小说《刺杀骑士团长》，小说上卷命名为“念头显露篇”，下卷命名为“隐喻改变篇”。 [2]  该作品的中译本首印达70万册，由于预售反响不俗又进行了加印"""

def stats_text_cn(text):
    # 文章字符串前期处理
    strl_ist=[]
    for i in text:
        strl_ist.append(i)
    
    count_dict = {}
    # 如果字典里有该单词则加1，否则添加入字典
    for text in strl_ist:
        if text in count_dict.keys():
            count_dict[text] = count_dict[text] + 1
        else:
            count_dict[text] = 1
    #按照词频从高到低排列
    count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
    return count_list
print (stats_text_cn(text))