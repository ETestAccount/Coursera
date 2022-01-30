#Defining a class
class Apple: #By convention,all classes starts with an upper case
    color = ""
    flavor = ""

jonagold = Apple() # to use our class,we create an instance of it called jonalgolde
jonagold.color = "Red"
jonagold.flavor = "Sweet"

print(jonagold.color)
print(jonagold.flavor)
print(jonagold.flavor.upper())