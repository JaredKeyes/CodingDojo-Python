#Assignment: Fun with Functions
'''
Create a series of functions based on the below descriptions.

Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number 
of that iteration and specify whether it's an odd or even number.

Your program output should look like below:
'''

#Odd/Even
def oddeven(y,z):
    for x in range(y,z):
        if(x % 2 == 0):
            print "The number is "+str(x)+". This is an even number."
        else:
            print "The number is "+str(x)+". This is an odd number."

oddeven(1,2001)

'''
Multiply:
Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a 
list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument. For example, let's say:
'''
#Multiply
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr

a = [2,4,10,16]
b = multiply(a,5)
print b

'''
Write a function that takes the multiply function call as an argument. Your new function should return the multiplied 
list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list. Here's 
an example:

def layered_multiples(arr):
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
'''
def layered_multiplier(arr):
    newArr = []
    for i in arr:
        entry =[]
        for count in range(0, i):
            entry.append(1)
        newArr.append(entry)
    return newArr

x = layered_multiplier(multiply([2,4,5],3))
print x


