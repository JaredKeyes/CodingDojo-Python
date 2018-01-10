words = "It's Thanksgiving day. It's my birthday,too!"

print words.find('day')
print words.replace('day', 'month')

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[-1]
newlist=[]
newlist.append(y[0])
newlist.append(y[-1])
print newlist

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
a = z[:len(z)/2]
b = z[len(z)/2-1:]
z = b
z[0]=a
print z