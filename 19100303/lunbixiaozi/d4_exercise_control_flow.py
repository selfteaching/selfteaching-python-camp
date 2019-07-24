print("#1: ")
for first in range(1,10):
    for second in range(1,10):
        if second <= first:
            result = first*second
            print (str(first) + "*" + str(second) + "=" + str(result), end = " ")
    print("\n")


print("#2: ")
for first in range(1,10):
    for second in range(1,10):
        if second <= first:
            result = first*second
            if(first%2!=0):
                print (str(first) + "*" + str(second) + "=" + str(result), end = " ")
    if(first%2!=0):
        print("\n")