#For loop printing all the odd numbers from 1 to 1000
'''
for count in range(1,1000):
    if(count % 2 == 1):
        print count
'''
#For loop printing all the multiples of 5 from 5 to 1,000,000
'''
for count in range(5,1000001):
    if(count % 5 == 0):
        print count
'''
#Getting the sum of all values in a list
'''
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b
'''
#Getting the average of all values in a list
'''
a = [1, 2, 5, 10, 255, 3]
b = sum(a)/len(a)
print b
'''