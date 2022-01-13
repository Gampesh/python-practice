class WomenWhoCode(object):
    raise_seat = 1
    _private_variable = 2
    __super_private = 10

    def __init__(self, first, last, seats):
        self.first_name = first
        self.last_name = last
        self.seats = seats
        self.email = first+'.'+last+'@cdk.com'


    def increaseSeats(self):
        self.seats = self.seats + self.raise_seat

    def fullName(self):
        return self.first_name+" "+self.last_name

    @staticmethod
    def noArg_0():
        print ("boom")

    @classmethod
    def classMethod(cls, member_str):
        firstName, lastName, seats = member_str.split('-')
        return cls(firstName,lastName, seats)


member1 = WomenWhoCode('Gampesh', 'Sahu', 1)
member2 = WomenWhoCode('Gampeshwar', 'Sahu', 12)
member1.someVar = '007'
member1.raise_seat = 10;
print(member1.raise_seat)
print(member2.raise_seat)

# print (WomenWhoCode)
# print (' ============================== ')
# print ( dir(WomenWhoCode) )
#
# print (member1)
# print (member1.someVar)
# print (member1.first_name)
# print (member1.last_name)
# print (member1.email)
#
# print ("============================================")
# print (member1.seats)
# member1.increaseSeats()
# print (member1.seats)
print ("============================================")
#someObj = member1.classMethod('gampesh-sahu-1') // Not prefferd way
someObj = WomenWhoCode.classMethod('gampesh-sahu-1')
print(someObj.first_name)
#
# print (member1.fullName())
# print (WomenWhoCode.fullName(member1)) # other way to call class method
# print ("====================Static method========================")
# member1.noArg_0()
# WomenWhoCode.noArg_0()
# print ("============================================")
#
# print (WomenWhoCode.raise_seat)
# #print (WomenWhoCode.__super_private) # This will not be accesible outside class
#
# print ('class.__dict__', WomenWhoCode.__dict__)
# print ('instance.__dict__', member1.__dict__)
# print ('Access super private variable', WomenWhoCode._WomenWhoCode__super_private)

# [start:stop:step]
a = [1,2,3,4]
print (a[::])
print (a[-1:])