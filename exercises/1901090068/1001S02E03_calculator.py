a=input('')
way=input('运算方法(1+ 2- 3* 4/)')
b=input('')
if int(way)==1:
    print (int(a)+int(b))
elif int(way)==2:
    print (int(a)-int(b))
elif int(way)==3:
    print (int(a)*int(b))
elif int(way)==4:
    print (int(a)/int(b))
else:
    print('Error')