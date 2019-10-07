from mymodule import stats_word

string = " 测试：今天是个好日子，好日子 126456220600 ，心想的事儿都能成，哈哈哈，都能成＃＄％＆＇（）＊＋，－／, the hao de wo kan xing xing wo wo @"


AAA = stats_word.stats_text(string)

print("统计 英文单词字频 和中文字频 的结果,并按从大到小排列：",AAA)
