# We looked at Control Flow and using if, elif, and else
# Control Flow syntax makes use of colons and identation (whitespace).
# This indentation system is crucial to Python and is what sets it apart from other programming languages.
'''
if some_condition:
    # execute some code
elif some_other_condition:
    # do something different
elif yet_another_condition:
    # do another thing
else:
    # do something else
'''

# We can have as many elifs as want

# Here is a basic if example
if 3>2:
    print('It\'s TRUE!')

hungry = True

if hungry:
    print('Feed me!') # We can use variables and if false nothing will print

# We looked at the else statement
hungry = False # hungry is already a boolean so we don't need to add == True

if hungry:
    print('Feed me!')
else:
    print("I'm not hungry")

# We then made some more complicated if statements

loc = 'Bank'

if loc == 'Auto Shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!')
else:
    print("I do not know much.")

print("I'm starting to hate VSC")

name = 'Sammy'
if name == 'Frankie':
    print('Hello Frankie!')
elif name == 'Sammy':
    print('Hello Sammy')
else:
    print("What is your name?")

# We can do some interesting things with variables
name = 'Adam'
print(len(name))

if len(name) > 0:
    print('Welcome', name + '!')
else:
    print('Welcome stranger!')

# We looked at For Loops in Python
# Many objects in Python are "iterable", meaning we can iterate over every element in the object.
# Such as every element in a list or every character in a string.
# We can use for loops to execute a block of code for every iteration.
# You can iterate over every character in a string, iterate over every item in a list, iterate over every key in a dictionary.

# Syntac for a loop
"""
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)
    
>> 1
>> 2
>> 3
"""

# An example of a for loop

mylist = [1,2,3,4,5,6,7,8,9,10]
for n in mylist:
    print(n)


# 'n' can be defined as anything

for bee in mylist:
    print('Hi')

# An example of an if and else statement

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

# An example of using a for loop to count

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)

# Here is what happens when indentation isn't done properly

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

    print(list_sum)

# Strings are a sequence so we can iterate through them

mystring = 'Hello World'

for letter in mystring:
    print(letter)

# We dont have to use variables for the strings

for l in "Hello World":
    print(l)

# We can use an underscore instead of a variable in a for loop
    
for _ in 'Hello World':
    print('Cool!')

# 

mylist = [(1,2), (3,4), (5,6), (7,8)]

for item in mylist:
    print(item)

# You technically don't need ()s here

for (a,b) in mylist:
    print(a)
    print(b)

# This is Tuple unpacking

mylist = [(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in mylist:
    print(b)

# With dictionaries, by default you iterate through the keys

d = {'k1':1, 'k2':2, 'k3':3}

for item in d:
    print(item)

# Here is how to print out the key:item pairs

d = {'k1':1, 'k2':2, 'k3':3}

for item in d.items():
    print(item)

for item,value in d.items():
    print(value) # Printing out just the values

# We then looked at While loops

# Syntax of a while loop
"""
while some_boolean_condition:
        #do something
    else:
        # do something different
"""

# Here is an example

x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1 # If we don't modify x, it will go on forever

# x += 1 is a more compact way of writing the above expression

x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print("X IS NOT LESS THAN 5")

# We can use break, continue, and pass statements in our loops to add additional functionality for various cases The three states are defined by:
# break: Breaks out of the current closes enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all.

x = [1,2,3]

for item in x:
    pass # Python expects something with the indent, a pass is a useful way to avoid the syntax error in this case

print('end of my script')

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        break
    print(letter)

x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

# We looked at Useful Operators

# We looked at range and its uses

for num in range(10):
    print(num) # Default starting number is 0

for num in range(3,10):
    print(num) # We can choose a starting number

for num in range(0,10,2):
    print(num) # We can add a step count at the end

range(0,10,2) # Will just return 'range(0, 10, 2)'

list(range(0,10,2)) # We can use range to define a list

# We looked at using the format function in for loops and calling variables

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1 # A variable is used for iteration

# Another example

index_count = 0
word = 'Adam'

for letter in word:
    print(word[index_count], '=', index_count)
    index_count += 1

# Using a for loop to enumerate

word = 'abcde'

for index,letter in enumerate(word):
    print(index,letter)

# We looked at zipping in python

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

zip(mylist1,mylist2) #Zips to a location and returns nothing

for item in zip(mylist1,mylist2):
    print(item) # Aggregates iterables into a tuple and returns them

# An example of zipping three lists together

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

list(zip(mylist1,mylist2)) # Using zip to create a list of tuples

for a,b,c in zip(mylist1,mylist2,mylist3):
    if a < 2:
        print(a,b,c) # choosing what list values we want
    else:
        print(a,b) # Example could be good for a high score

# Using in to return booleans

'x' in [1,2,3] # Returns false
'x' in ['x','y','z'] # Returns true
'mykey' in {'mykey':345} # Works with dictionaries

# We can use min and max for minimum and maximum values

mylist = [10,20,30,40,100]
min(mylist)
max(mylist)

# Importing the shuffle function from an included Python library
# This is an in place function, it returns nothing and if you assign it to a variable, the variable will have nothing and be a NoneType.
# It must be used on already defined lists or variables

from random import randint, shuffle

shuffle(mylist) # randomises list

# We looked at the random interger function
# randint has output and thus isn't an inplace function and can be used to assign a variable or just spit out a number

randint(0,100)
mynum = randint (0,10)
mynum

# We use input to take input, a key function of python

input('Enter a number here: ')

uname = input('Enter your name: ') 
+ str(randint(0,999))
print(uname)

# Input by default provides strings so we need to define floats and intergers

float(input('Enter a number here: '))

# We then looked at List Compregensions in Python
# List comprehensions are a unique way of quickly creating a list with Python.
# If you find yourself using a for loop along with .append() to create a list, List comprehensions are a good alternative
# Below is the typical way of using a for loop in Python

mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# There is much more efficient way to do this in Python
mylist = []

mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in 'word'] # Of course we can use it on strings
print(mylist)

# We can do more complicated list comprehensions

mylist = [num**2 for num in range (0,11)]
print(mylist)

# Here is another example using modulus

mylist = [x for x in range(0,11) if x%2==0]
print(mylist

# Here is an example of calculating temperature using list comprehension and thus few lines

celcius = [0,10,20,34.5]
fahrenheit = [((9/5) * temp + 32) for temp in celcius]
print(fahrenheit)

# Note how we can use different operators like if and else in list comprehensions

results = [ x if x%2==0 else 'ODD' for x in range (0,11)]
print(results)

# We looked at nested loops, loops that sit within other loops

mylist = []

for x in [2,4,6]:
    for y in [100,200,300]: 
        mylist.append(x*y)
print(mylist) # prints like x[0]*y[0], x[0]*y[1], x[0]*y[1] etc...

# List comprehension will condense this but make its readability harder

mylist = [x*y for x in [2,4,6] for y in [100,200,300]]
print(mylist)
