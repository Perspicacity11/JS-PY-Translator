import math

print("Cassius Naylor")
print('o----')
print(' ||||')

name = input('What is your name? ')
print('Hi ' + name)
colour = input('What is your favourite colour? ')
print(name + "'s favourite colour is " + colour)
print(f'{name} favourite colour is {colour}') #interpolation must be preceded with an f

birth_year = input('What year were you born? ')
age = 2023 - int(birth_year)
print(age)

email = '''Hello,
        I hope this finds you well.
        I am emailing about something.
        Best,
        Cassius'''

print(email)

print(email[2]) #third index element
print(email[0:3]) #first to fourth index element
print(email[0:]) #all elements past first
print(email[:7]) #all elements up to eighth

another_email = email[:] # copy one variable into another
print(another_email)

print(len(another_email)) # gives length of another_email

print(email.upper())
print(email.lower())

print(email.find('C')) #finds index position of letter C
print(email.replace('something', 'nothing')) #replaces something with nothing

print('emailing' in email) #evaluates true due to the presence of the substring 'emailing' in email string

print(math.floor(2.9))

# CONDITIONALS

is_hot = True #boolean values are capitalised in Python
is_cold = False
is_rainy = True

if is_hot:
    print('It is hot')
elif is_cold:
    print('')
elif is_hot and is_cold:
    print('Uncertain weather')
elif is_hot and not is_rainy:
    print('Sunglasses')
else:
    print('It is not hot')


#LOOPS

i = 1
while i <= 5:
    print(i)
    i = i + 1
    if i == 3:
        break #breaks loop on fulfilment of nested conditional
else: #breaks loop on fulfulment of loop condition
    print('Reached end of counter')



for letter in 'Python':
    print(letter)
#This will print each letter in the string Python on a new line


for name in ['Cass', 'James', 'Max']:
    print(name)
#This will print each name in the list on a new line


for number in range(10):
    print(number)
#range function creates an array object of numbers, which are then iterated through

for number in range(5, 10):
    print(number)
#same idea but starting at 5

for number in range(2, 20, 2):
    print(number)
#same idea but goes from 2 to 20 with increments of 2 (2, 4, 6, 8, etc)


for x in range(4):
    for y in range(3):
        print(f'({x}, {y}')
#inner loop runs for the full range on the first iteration of x, and then increments x and does it again


numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''
    for num in range(x_count):
        output += num
    print(output)


# Lists (arrays)

# Multidimensional arrays are called '2D lists' in Python

numbers = [1, 4, 6, 8, 8, 11, 20]

numbers.append(10) #adds the argument to the end of the list
numbers.insert(0, 10) #adds the second argument at the index position of the first
numbers.remove(6)
numbers.clear() #empties the list
numbers.pop() #removes the last element
numbers.index(4) #returns the index of number 4 in the list
numbers.count(8) #counts the number of instances of number 8 in the list
numbers.sort() #sorts the number IN PLACE (mutates the original list), returns nothing
numbers.reverse()
numbers2 = numbers.copy() #copies numbers list one to a new list called numbers2

print(50 in numbers) #will return false based on the absence of the number 50 from the list
print(20 in numbers) #evaluates true for the same reason


uniqueNumbers = []
for number in numbers:
    if number not in uniqueNumbers:
        uniqueNumbers.append(number)
#The above only saves numbers that do not appear more than once to the new uniqueNumbers list


# Tuples

# Similar to lists but they cannot be changed (they are immutable)
# Tuples are defined with round brackets, lists with square brackets
# Tuples only have information methods like count and index


# Unpacking (object destructuring)

coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
#This is an unweildly way to destructure the list object

x, y, z = coordinates
#This achieves the same outcome with much less code


#Dictionaries (hashes or JS objects)

phoneNumber = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for number in phoneNumber:
    output += digits_mapping.get(number, "!")
print(output)

# The above receives a phone number as input, iterates through its individual integers and uses .get (a dictionary
# method, returns 'none' if the key doesn't exist, rather than throwing an error) to grab the value
# set against the key of that integer, before appending it to the output string
# The second argument provided to .get is the default value to append if the number doesn't have a corresponding
# value in the dictionary

# Functions

def say_hi():
    print('Hi')


def add_numbers(x, y):
    print(x + y)

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')

greet_user("John", "Smith")
greet_user(last_name="Smith", first_name="John")
# The second is using keyword arguments, which fill the function regardless of the order of parameters or arguments;
# Useful when supplying integers as arguments, which might have unclear meaning on their own
# IMPROVES READABILITY
# Positional arguments have to come before keyword arguments when the function is called

# No implicit return in Python

# Error handing

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")

# After the 'except', state the type of error you want to catch and how to deal with it


# Classes

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, my name is {self.name}")


cass = Person("Cassius")
cass.talk()
# Prints 'Hi, my name is Cassius'
# First parameter of any class method (including the constructor) is self

class Developer(Person):
    pass

# The above notation allows the Developer class to inherit the talk method from the Person superclass
# Pass allows you to save an otherwise empty class that inherits its methods from a superclass without Pycharm
# faulting the empty class

import main

print(main.print_hi("Cassius"))
# This imports the print_hi method from the main.py file

from main import print_hi

print(print_hi("Cassius"))

# If you're only importing one method from an external module, the second option is cleaner as you don't need to
# call the module name to call the method