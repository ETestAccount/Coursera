class Piglet:
    name = "piglet"
    def speak(self): #a function inside of a class is called method. this represent the instance of the class
        print("Oink! i'm {} Oink".format(self.name))

#Creating an instance of class
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

print(100*"_")
print("Example 1: Creating another function")

class Piglet2:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = Piglet2()
piggy.years = 2
print(piggy.pig_years())