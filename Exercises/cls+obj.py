# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "Red"
car1.kind = "Convertible"
car1.value = "60.000"

car2 = Vehicle()
car2.name = "Jump"
car2.color = "Blue"
car2.kind = "Van"
car2.value = "10.000"

# test code
print(car1.description())
print(car2.description())