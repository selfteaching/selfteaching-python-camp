print("�žų˷���")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, "*", j, "=", i* j, end="\t")
    print()

print("����ż���ľžų˷���")
i = 1
while i < 10:
    if i % 2 == 0:
        print()
    else:
        for j in range(1, i + 1):
            print(i, "*", j, "=", i * j, end="\t")
    i +=1