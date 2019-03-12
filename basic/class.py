class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):                #Initiating class
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {}={}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood,hamilton))

print(hamilton.on)          #return False
hamilton.switch_on()        #turning on with switch_on fucntion
print(hamilton.on)          #return True

Kettle.switch_on(kenwood)
print(kenwood.on)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)
kenwood.power_source = "gas"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)                  #Find possible functions for Kettle class
print(kenwood.__dict__)
print(hamilton.__dict__)
