#Optional Assignment: Multiplication Table
#Create a program that prints a multiplication table in your console.

n=12
for row in range(1,n+1):
    print(*("{:3}".format(row*col) for col in range(1, n+1)))