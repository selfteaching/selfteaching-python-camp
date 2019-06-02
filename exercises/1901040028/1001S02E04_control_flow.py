#for i in range(1,10):#定义行，确定第几行
#    for j in range(1,i+1):#定义列，使列<=行，确定该行共有多少列，先完成内层循环后，再做外层循环。i=1时，j=1时，打印出1×1，i=2时，j=1打印出结果，再循环为j=2，依次类推
 #       print(j,"×",i,"=",j*i,"\t",end='')
  #  print()




i=0

while i<9:
    i=i+1
    if i%2==0: 
        continue
    j=1
    while j<=i:
        print(i,"×",j,"=",i*j,"\t",end=" ")
        j+=1
    print()


    