class Call(object):
    def __init__(self,id,name,number,time,reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print self.id
        print self.name
        print self.number
        print self.time
        print self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0

    def add(self, caller):
        self.calls.append(caller)
        self.queue += 1
        return self
    
    def remove(self):
        self.calls.pop(0)
        self.queue -= 1
        return self

    def info(self):
        print "list size", self.queue
        for count in self.calls:
            print " "
            print "caller:", count.name
            print "number:", count.number
            print "call time:", count.time
            print "reason to call:", count.reason
            print " "

        return self

caller1 = Call(1,"Nick","772-608-2693","5:00 AM","I live here.")
caller2 = Call(2,"Zach","996-301-1099","7:59 AM","I am the false God!")
caller3 = Call(3,"Steven","595-240-2594","8:00 AM","What's up?")
callcenter1 = CallCenter()
callcenter1.add(caller1).add(caller2).add(caller3).info().remove().info()