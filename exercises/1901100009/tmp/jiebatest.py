import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("小荷才露尖尖角")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("大师们的写作课，新媒体写作课，巨土文化")  # 搜索引擎模式
print(", ".join(seg_list))

