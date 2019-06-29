from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print (dict(c))

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
#Counter({'a': 2})
print(c | d)
