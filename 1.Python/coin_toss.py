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