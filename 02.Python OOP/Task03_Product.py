class Product(object):
    def __init__(self,price,name,weight,brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    
    def sell(self):
        self.status = "Sold"
        return self
    def tax(self):
        tax = self.price *.06
        self.price = self.price + tax
        return self
    def returnitem(self,y):
        if(y=="defective"):
            self.status = "defective"
            self.price = 0
        elif(y=="mint"):
            self.status = "For Sale"
        elif(y=="opened"):
            self.status = "Used"
            self.price = self.price *.8
        else:
            print "Not a valid reason for return"
        return self
    def displayinfo(self):
        print self.price
        print self.name
        print self.weight
        print self.brand
        print self.status
        return self

product1 = Product(20,"Bob's Burgers","5 lbs","Bob Co.")
product1.displayinfo().tax().sell().displayinfo().returnitem("defective").displayinfo()

