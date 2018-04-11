#Optional Assignment: Foo and Bar
'''
Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime 
number, print "Foo". If it is a perfect square, print "Bar". If it is neither, print "FooBar". Do not use the python 
math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it 
is a perfect square. It is, so print "Bar".
'''

def checkPrime(i):
    flag = True
    for x in range(2,9):
        if(i == x):
            continue
        if(i % x == 0):
            flag = False
    return flag

def checkSquare(i):
    flag = False
    return flag

for i in range(1,20):
    flagfoo = checkPrime(i)
    flagbar = checkSquare(i)
        
    if(not flagfoo and  not flagbar):
        print(str(i) + " " + "Foobar")
    else:
        print(str(i) + " " + "Foo")
    
    