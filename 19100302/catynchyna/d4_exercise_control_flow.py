# my first thought about using "break" trapped me and I dont know how to change lines

print ("Oh My Stitched 9x9 Table\n")
for x in range(1, 10):
    for y in range(1, x+1):
        print("{}*{}={}".format(x,y,x*y),end='\t')
    if x == y :
        print() #this statement stands for change another line?


# while usage
print ("""
**Oh My Stitched Table without EVENx**\n
""")

for x in range(1, 10, 1):
    for y in range(1, x+1, 1):
        while x % 2 == 0:
            if x == y :
                print() #this statement stands for change another line?
            break
        else:
            print("{}*{}={}".format(x,y,x*y),end="\t")

    
    #print("\n") #this statement stands for change another line?
    # this table looked different, what was the problem of the lines?[to be checked myself]