#for循环
for a in range(1,10):
    for b in range(1,a+1):  
        c=a*b
        print(f"{a}*{b}={c}",end="\t")
    print()



#while循环
i=0
while i < 10:
    i +=1
    for a in range(1,i+1):   
        if i % 2 == 0: 
            continue
        j =a * i
        print(f"{i}*{a}={j}",end="\t")   
    print()