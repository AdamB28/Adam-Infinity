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