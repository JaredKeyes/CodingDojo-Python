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

#Multiply
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
'''
a = [2,4,10,16]
b = multiply(a,5)
print b
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


