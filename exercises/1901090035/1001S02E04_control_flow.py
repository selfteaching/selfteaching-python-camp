
# 九九乘法表

'''先找到99乘法表怎么算。自己想真的想不出来，上星期在百度上搜到过答案，现在还有印象，就自己试着写了出来。'''
'''for a in range(1,10):#a
    for b in range(1,a+1):#b
        print(a,"*",b,"=",a*b)'''



'''分行。这个试了好几次，没有花费太大力气，我是先试，在整理思路，这个方式不好。应该现有思路，在试.'''

for a in range(1,10):#a
    for b in range(1,a+1):#b
        if b<a:
            print(a,"*",b,"=",a*b,end='\t')

        if b==a:
            print(a,"*",b,"=",a*b,)
        
        
    
        

    
            
        


