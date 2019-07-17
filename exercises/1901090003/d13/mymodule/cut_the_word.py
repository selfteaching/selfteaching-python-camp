import jieba

text = '''智叟聽了，無話可說：
二山的守護神被愚公的堅毅精神嚇倒，便把0此事奏知天帝。天帝佩服愚公的精神，就命兩位大力神揹走二山12。
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who
'''
n = [x for x in jieba.cut(text) if len(x)>2]

print(' '.join(n))


