class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health =  health
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def display_health(self):
        print self.health
        return self
    def display_name(self):
        print str(self.name)
        return self
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a dragon"
class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name,100)

dog1 = Dog("Dog")
dragon1 = Dragon("Dragon")
cat1 = Cat("Cat")

dog1.display_name().pet().pet().walk().display_health()
dragon1.display_name().fly().fly().fly().display_health()
cat1.display_name().display_health()