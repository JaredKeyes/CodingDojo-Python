#Assignment: Find Characters
'''
Write a program that takes a list of strings and a string containing a single character, and prints a new list of all 
the strings containing that character.

Here's an example:
'''

word = ['hello','world','my','name','is','Anna']

char = 'o'
newList = []

for idx in range(0 , len(word)):
    if word[idx].find(char) > -1:
        newList.append(word[idx])
print newList
