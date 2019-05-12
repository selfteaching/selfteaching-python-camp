
replacedText = text.replace("better", "worse")
# print(replacedText)

splitReplacedText = replacedText.split()
removedEaText = []

for i in splitReplacedText:
	i=re.sub(r'[^a-zA-Z\']',"",i)
	#print(i)
	if 'ea' not in i:
		if i == '':
			continue
		else:
			removedEaText.append(i)

print('\n\n')
print(removedEaText)

swappedCaseText = []
for i in removedEaText:
	swappedCaseText.append(i.swapcase())

print('\n\n')
print(swappedCaseText)

print('\n\n')
print(sorted(swappedCaseText))

import re 

