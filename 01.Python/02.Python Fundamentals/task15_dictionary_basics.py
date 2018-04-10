#Assignment: Making and Reading from Dictionaries
'''
Create a dictionary containing some information about yourself. The keys should include name, age, country 
of birth, favorite language.

Write a function that will print something like the following as it executes:

My name is Anna
My age is 101
My country of birth is The United States
My favorite language is Python

There are two steps to this process, building a dictionary and then gathering all the data from it. Write a 
function that can take in and print out any dictionary keys and values.
'''

info = {"My name is":"Jared","My age is":"27","My country of birth is":"USA","My favorite language is":"English"}

for key,data in info.iteritems():
    print key, data 