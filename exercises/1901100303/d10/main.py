from collections import Counter

cnt = Counter()
for word in ['red','blue','red','green','blue','green']:
    cnt[word] += 1                           ##########---这一行怎么理解？
print(cnt)
