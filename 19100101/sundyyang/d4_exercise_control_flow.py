#output “Multiplication Table” by “for xx in"

for i in range(1,10):
     for j in range(1,i+1):
         print( i,"*", j,"=" ,i*j,end="\t")
     print (end="\n")

print (end="\n")

i=1
while i<10:
    j=1
    if(i%2==1):
        while j<i+1:
            print( i,"*", j,"=" ,i*j,end="\t")
            j=j+1
        print (end="\n")
        i=i+1
    else:
        i=i+1
