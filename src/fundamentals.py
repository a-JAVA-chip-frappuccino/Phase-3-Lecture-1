# variables and data types
    # string concatenation: "string1" + "string2"
    # f-string interpolation: f"{string1}{string2}"

    # typecasting: changing one data type to another

'''
first_name = "Eleanor"
last_name = "Kelman"

favorite_number = -7
print(first_name + "'s favorite number is " + str(favorite_number))
print(f"{first_name}'s favorite number is {favorite_number}")
'''

# conditional statements
'''
if first_name == "Eleanor":
    print("Hello there, Eleanor!")

if first_name == "Tyler" or last_name == "Taylor":
    print("Hello there, Tyler!")
else:
    print("You're not Tyler!")

if favorite_number < 0:
    print("The number is negative!")
elif favorite_number == 0:
    print("The number is exactly 0!")
else:
    print("The number is positive!")

if favorite_number < 0:
    print("The number is negative!")
if favorite_number == 0:
    print("The number is exactly 0!")
if favorite_number > 0:
    print("The number is positive!")

# ternary operator
print("The number is a big number!") if favorite_number > 5 else print("The number is a small number!")
'''

# loops and sequences
    # for loops: run for duration of a sequence
    # while loops: run for so long as a condition is met

'''
for i in range(10):
    print(i)

print("")

for i in range(5, 10):
    print(i)

print("")

for i in range(5, 10, 2):
    print(i)

for i in range(7, 0, -1):
    print(i)

counter = 0

while counter < 10:
    print(counter)
    counter = counter + 1 # counter += 1

secret_word = ""

while not secret_word == "you guessed it":
    secret_word = input("Guess the secret word (it's actually a sentence muahahaa)")

while_loop_counter = 0

# WEEOOWEEOO DANGER INFINITE LOOP ALERT!
while True:
    print("lmao")
    if while_loop_counter > 6:
        break # exits a loop prematurely
    while_loop_counter += 1

'''

# functions

'''
# function definition
def prints_hello_world():
    print("hello world")

# function call
prints_hello_world()

def prints_hello_to_you(name):
    print("Hello, " + name)

prints_hello_to_you("Mario")
prints_hello_to_you("Luigi")

def adds_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
    return num1 + num2

sum = adds_two_numbers(3, 4)
print(sum)
'''