# lists and list comprehension
    # lists are mutable
    # lists are 0-indexed and store ordered values

'''
nums = [1, 2, 3, 4, 5]

# slice: [starting index : ending index]

nums.append(6) # adds new element to end of list

nums.pop(5) # removes (and retrieves) element from given index of list

# forEach loop
for num in nums:
    print(num)

nums_squared = []

for num in nums:
    nums_squared.append(num * num)

nums_squared = [num * num for num in nums] # list comprehension version

nums_cubed = []

for num in nums:
    if num % 2 == 0:
        nums_cubed.append(num * num * num)

nums_cubed = [num ** 3 for num in nums if num % 2 == 0] # list comprehension version

print(nums_cubed)
'''

# dictionaries
    # dictionaries are mutable
    # dictionaries store unordered key:value pairs

'''
squares = {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}

print(squares[4])

squares[6] = 36 # adds new key:value pair

print(squares)
'''

# sets
    # sets are mutable
    # sets are unordered and without repeat values

'''
plants = set()

plants.add("tree")
plants.add("bush")
plants.add("flower")
plants.add("grass")
plants.add("bush") # will not be added (repeat value)

print(plants)
'''

# tuples
    # tuples are immutable
    # tuples are 0-indexed and store related values

'''
color = (9, 18, 200)

print(color)
'''