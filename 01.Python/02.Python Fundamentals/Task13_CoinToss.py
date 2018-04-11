#Assignment: Coin Tosses
'''
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the 
head/tail appears.

Sample output should be like the following:

Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you!
'''

def cointoss(x,y):
    counthead = 0
    counttails = 0
    for x in range(x,y):
        import random
        randomnum = random.randint(1,2)

        if(randomnum == 1):
            counthead = counthead + 1
            print "Attempt number",x,"Throwing a coin... It's a head! ... Got",counthead,"head(s) so far and",counttails,"tail(s) so far"
        else:
            counttails = counttails + 1
            print "Attempt number",x,"Throwing a coin... It's a tails! ... Got",counthead,"head(s) so far and",counttails,"tail(s) so far"

cointoss(0,10)