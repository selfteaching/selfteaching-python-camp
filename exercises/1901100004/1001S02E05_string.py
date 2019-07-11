sample_text =
text = sample_text.replace('better','worse')
print('将字符串样本里的 better 全部替换成 worse ==>', text)
words = text.split()
filtered = []
for word in words:
    if word.find('ea') < 0:
        filtered.append(word)
print('将单词中包含 ea 的单词剔除 ==》'，filtered)
swapcased = [i.swapcased() for i in filtered]
print('进行大小翻转 ==》'，swapcased)
print('单词按 a...z 升序排列 ==》'，sorted(swapcased))