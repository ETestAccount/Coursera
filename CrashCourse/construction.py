class Apple:
    def __init__(self, color, flavor):#this is a method construct that get called when the instance of the class is called
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
    
jonagald = Apple("red","sweet")
print(jonagald)

