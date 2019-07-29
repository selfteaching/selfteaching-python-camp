
template = '''
If you were to take a blind survey of investors, most would tell you that corporate earnings are a rare bright spot in a landscape increasingly riddled with macro headwinds.
Ed Clissold, the chief US equity strategist at Ned Davis Research, doesn't necessarily disagree. But he does think investors are taking that information and drawing the wrong conclusion.
It's a common misconception that historically strong profit growth translates directly to a bright future for a company's stock, Clissold says. He argues instead that, at such lofty levels, there's often nowhere for earnings to go but down - something that doesn't bode well for a firm's shares.
习近平指出，国际形势发生了很大变化，但中法关系始终保持高水平健康稳定发展。总统先生就任以来，两国关系在不到两年时间里又迈上了新台阶，取得很多新成果。今年是一个具有特殊纪念意义的年份，既是中法建交55周年和中国留法勤工俭学运动100周年，也是新中国成立70周年。知古可以鉴今，为了更好前行。当今世界正经历百年未有之大变局，人类处在何去何从的十字路口，中国、法国、欧洲也都处于自身发展关键阶段。中方愿同法方一道，传承历史，开创未来，使紧密持久的中法全面战略伙伴关系继续走在时代前列，共同为建设一个持久和平、普遍安全、共同繁荣、开放包容、清洁美丽的世界作出更多历史性贡献。
'''

#判断英文
def stats_text_en(checkstr):
	endic = {}
	for ch in checkstr:
		if u'a' <= ch <= u'z' or u'A' <= ch <= u'Z':
			endic[ch] = checkstr.count(ch)
	return endic

#判断中文
def stats_text_cn(checkstr): 
	cndic = {}
	for i in checkstr:
		if u'\u4e00' <= i <= u'\u9fff':
			cndic[i] = checkstr.count(i)
	return cndic


def main():
	cndic = stats_text_cn(template)             #调用检索中文频次的函数

	cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True)      #从大到小排序
	print(cndic)                            

	endic = stats_text_en(template)             #调用检索中文频次的函数

	endic=sorted(endic.items(),key=lambda item:item[1],reverse = True)      #从大到小排序
	print(endic)                           


if __name__ == '__main__':
	main()
