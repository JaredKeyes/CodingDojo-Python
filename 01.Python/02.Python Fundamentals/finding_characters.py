word = ['hello','world','my','name','is','Anna']

char = 'o'
newList = []

for idx in range(0 , len(word)):
    if word[idx].find(char) > -1:
        newList.append(word[idx])
print newList
