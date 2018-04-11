class Bike(object):
    def __init__(self,price,maxspeed):
        self.price = price
        self.maxspeed = maxspeed
        self.miles = 0
    def displayinfo(self):
        print "Price:",self.price
        print "Max speed:",self.maxspeed
        print "Miles",self.miles
        return self
    def ride(self):
        print "Riding..."
        self.miles = self.miles + 10
        return self
    def reverse(self):
        print "Reversing..."
        self.miles = self.miles - 5
        return self

bike1 = Bike(200,50)
bike2 = Bike(300,100)
bike3 = Bike(1000,1)

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()