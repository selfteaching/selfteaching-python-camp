

def stats_text_cn(text, count):  # 统计中文词频，增加变量count控制输出
	    """Count the chinese words in the text """  # 使用文档字符串说明
	    from collections import Counter  #调用Counter计数器
	    from collections import Counter  # 调用Counter计数器
	    import jieba
	    if not isinstance(text, str):  # 如果不是字符串类型触发异常
	        raise ValueError("input data is not string type")
	    text = [x for x in jieba.cut_for_search(text) if len(x) >= 2]  #使用精确模式分词
	    countcn = {}
	    count = int(count)
	    for i in text:
	        if u'\u4e00' <= i <= u'\u9fff':
	            countcn[i] = text.count(i)
	
	    countcn = Counter(countcn).most_common(count) #按词频排序并用count控制输出
	    countcn = Counter(countcn).most_common(count)  # 按词频排序并用count控制输出
	    return countcn

