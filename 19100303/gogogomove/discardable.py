text = "I'm a hand some boy and hand with hand boy I'm!"

frequency = {}

for word in text.split():
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1
print(frequency)

