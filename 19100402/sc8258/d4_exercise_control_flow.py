for i in range(1,10):
    #print(i,end = "")
    for j in range(1,i+1):
        print('%s*%s=%s'%(i,j,i*j),end = '')
    print()   
    

s=1
while s <=9:
     if s % 2!= 0:
          c = 1
          while c > s + 1:
              print(s,"*",c,'=',s*c,sep="",end="\t")
              c += 1
          print()
     s += 1

