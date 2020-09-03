class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def hatdog(self):
        self.price = 19
        return 'hatdog'

    def switch_on(self):
        self.on = True

kenwood = Kettle('kenwood', 15)

print(kenwood.hatdog())
print(kenwood.price)
Kettle.switch_on(kenwood)
print(kenwood.on)

kenwood.wheel = "toyota"
print(kenwood.wheel)
