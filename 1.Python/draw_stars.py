
def draw_stars(list):
    for i in list:
        if (isinstance(i, int)):
            print "*" * i
        elif (isinstance(i, basestring)):
            print i[0] * len(i)



draw_stars([1,2,3, "No", "Yes"])