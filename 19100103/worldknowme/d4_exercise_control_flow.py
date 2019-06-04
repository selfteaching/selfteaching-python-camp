print('九九乘法口诀表如下：')
a=[1,2,3,4,5,6,7,8,9]
b=[1,2,3,4,5,6,7,8,9]
for n in a :
    if n<10:
       for m in b:
          if m<10:
             if n>=m:
                print (n,'*',m,'=',n*m,' ',end='')
                if n==m:
                   print ('')
           
print('去掉偶数行的九九乘法口诀表如下：')
c=0
d=1
while c<9 :
    c=c+1 
    while d<=c:
       if c%2==1:
              
          print (c,'*',d,'=',c*d,' ',end='') 
          if c==d:
             print(' ')
       d=d+1
    else:
       d=1    
                  
print('结束啦,嘿嘿嘿~~~~~~')
   
      
      
          
         
           
