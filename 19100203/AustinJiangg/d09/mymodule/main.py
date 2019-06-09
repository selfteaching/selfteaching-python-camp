'''from stats_word import stats_text_cn
stats_text_cn(1234)

while True:
    try:
        x = input("Please enter a text: ")
        stats_text_cn(x)
        break
    except ValueError:
        print("Oops! Argument text must be <class 'str'>  Try again...")
'''
from collections import Counter
file1= open('tang300.txt', 'r')
text = file1.readlines()
file1.close()
dict1 = {}
for i in text:
    if i in ['」','「','!','-','’',' ','\n',',','，','.','，','。','”','“','※','…','？','：','！','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
        continue
    if i not in dict1:        #为首次出现的字创建key
        dict1[i] = 0
    dict1[i] += 1
print(Counter(dict1).most_common(100))
