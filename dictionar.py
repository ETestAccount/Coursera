file_counts={"jpf":10, "txt":12, "csv":2, "py":23}

print(file_counts["txt"])
file_counts["cfg"] = 9
file_counts["csv"] = 17

#deleting a key
del file_counts["cfg"]
print(file_counts)

print(100*"_")
print("Example 1: loop throught a dictionary")
file_counts={"jpf":10, "txt":12, "csv":2, "py":23}
for ext in file_counts:
    print(ext)


print(100*"_")
print("Example 1: loop throught a dictionary with values and keys")
file_counts={"jpf":10, "txt":12, "csv":2, "py":23}
for ext, amount in file_counts.items():
    print("There are {} file with the .{} extention".format(amount, ext))

print(file_counts.keys())
print(file_counts.values())

print(100*"_")
print("Example 1: How many times letters appears in a text")
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaaaa"))
print(count_letters("This is a very long letter in a string"))