# Define function
def Multiplication(x, y):
   """Multiplication"""
   
   return x * y
   
# Task#1
   
for i in range(1,10,1):
    for j in range(1,i+1,1):
        print(i,"*",j,"=", Multiplication(i, j),"      ",end="")
    print("")
print("")
	
# Task#2

i=1
while i<10:
    if i%2==1:
        j=1
        while j<=i:
           print(i,"*",j,"=", Multiplication(i, j),end="\t")
           j=j+1
        print("")
    i=i+1
    