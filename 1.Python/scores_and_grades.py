for x in range(0,10):
    import random
    randomnum = random.randint(60, 100)
    if(randomnum >= 90):
        print "Score:"+str(randomnum)+"; Your grade is A"
    elif(randomnum >= 80):
        print "Score:"+str(randomnum)+"; Your grade is B"
    elif(randomnum >= 70):
        print "Score:"+str(randomnum)+"; Your grade is C"
    else:
        print "Score:"+str(randomnum)+"; Your grade is D"