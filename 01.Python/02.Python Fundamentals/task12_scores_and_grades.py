#Assignment: Scores and Grades
'''
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function 
should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
'''

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