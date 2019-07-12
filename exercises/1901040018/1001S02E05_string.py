text='''
'''
text1=text.replace('better','worse')
print(text1)

text2=text1.split()
text3=[]
    for i in text2:
        if i.find('ea')<0:
        text3.append(i)
print(text3)

text4=''.join(text3)
print(text4)

text5=text4.swapcase()
print(text5)
