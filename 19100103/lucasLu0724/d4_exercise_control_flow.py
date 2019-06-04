print("that's lucas D4 homework")
nums=[1,2,3,4,5,6,7,8,9]
nums2=[1,2,3,4,5,6,7,8,9]
nums3=[9,8,7,6,5,4,3,2,1]
print("使用for实现的九九乘法表")
for t in nums:
    y=nums2[:t]
    for r in y:
        if r==y[-1]:
            print("{0}*{1}=".format(t,r),t*r)
        else:
            print("{0}*{1}=".format(t,r),t*r,end='\t')

print("使用while 实现的九九乘法表")
i=1

while i <=9:
    j=1
    if i%2==0:
        i+=1
        continue
    print()
    while j<=i:
        print("{0}*{1}=".format(i,j),i*j,end="\t")
        j=j+1
    i=i+1


    