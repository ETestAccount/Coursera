multiples = []
for x in range(1, 11):
    multiples.append(x*7)
print(multiples)


print(100*"_")
print("Example 3: Using list comprehension")
multiplsx = [x*7 for x in range(1,11)]
print(multiplsx)

print(100*"_")
print("Example 3: Using list comprehension")
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

print(100*"_")
print("Example 4: Using list comprehension")
z = [x for x in range(0,101) if x % 3 == 0]
print(z)