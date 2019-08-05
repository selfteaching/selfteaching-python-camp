text = '''
The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit.
Simple is better than complex. Complex is better than complicated.
'''

list = text.split()
print(list)
result = []
for i in list:
    temp = ""
    for j in i:
        if j.islower():
            j = j.upper()
        elif j.isupper():
            j = j.lower()
        temp = temp + j
    print(temp)
    i = temp
    #n = list.index(i)
    print(text)
    result.append(i)
print(result)
        