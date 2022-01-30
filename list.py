animals = ["lion","Zebra","Dolphin", "Monkeyu"]
chars = 0
for animal in animals:
    chars +=len(animal)

print("Total Characters: {}, Average Length; {}".format(chars, chars/len(animals)))

print(100*"_")
print("print index value of the list")
winners = ["Ashely", "dylan","Rese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person)) #index + 1 makes the incident start from 1. this get the index of the values


print(100*"_")
print("Working on email with list of people")
def full_emails(people):
    result = [] #variable created for return value
    for email, name in people: #unpack the variable in emails and people
        result.append("{}<{}>".format(name, email))
    return result

print(full_emails([("alex@example.com","Alex Diego"), ("Shay@example.com", "Shay Brandt")]))
