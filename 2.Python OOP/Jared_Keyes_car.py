class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if(self.price>=10000):
            y = 0.15
        else:
            y = 0.12
        self.tax = y
        self.display_all()

    def display_all(self):
        print "Price:",self.price
        print "Speed:",self.speed
        print "Fuel:",self.fuel
        print "Mileage",self.mileage
        print "Tax:",self.tax
        return self

car1 = Car(2000,300,"Not full","12mpg")
car2 = Car(10000,200,"Full","500mpg")
car3 = Car(2000,300,"Not full","12mpg")
car4 = Car(10000,200,"Full","500mpg")
car5 = Car(2000,300,"Not full","12mpg")
car6 = Car(10000,200,"Full","500mpg")