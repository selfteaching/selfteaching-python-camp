text = "hellO"
temp = ""
for j in text:
    
    if j.islower():
        j = j.upper()
    elif j.isupper():
        j = j.lower()
    print(j)
    temp = temp + j
    print(text)
text = temp
print(text)