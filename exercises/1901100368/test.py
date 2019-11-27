squares = []
test = "Although never is , often better than *right* now."
a = tuple(test)
j = 0
print(a)
for i in range(len(test)):
    if test[i] == "," | test[i] == "." | test[i] == "*" | test[i] == "'":
        continue
    else:
        squaresa = test[i] + squaresa
        print(squaresa)
        #squares[j]+ = test[i]

#        continue
    #else:
     #   squares.append(test[i])
#print(squares)