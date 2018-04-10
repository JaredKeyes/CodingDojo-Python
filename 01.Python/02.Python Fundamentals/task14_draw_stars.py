#Assignment: Stars
'''
Write the following functions.
Part I
Create a function called draw_stars() that takes a list of numbers and prints out *.
Part II
Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() 
function. When a string is passed, instead of displaying *, display the first letter of the string according
to the example below. You may use the .lower() string method for this part.
'''
def draw_stars(list):
    for i in list:
        if (isinstance(i, int)):
            print "*" * i
        elif (isinstance(i, basestring)):
            print i[0] * len(i)



draw_stars([1,2,3, "No", "Yes"])