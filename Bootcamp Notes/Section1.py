# This is a comment, it uses # to begin
# We started with basic printing of strings
print('hello')

# We did a bit on maths operators, for example:
print(2 + 2); print(2 - 2); print(2 * 2); print(2 / 2)
print(110 % 100) # This is modulus which is used for remainders
print(2 ** 5) # This is used for powers
print((1 + 2) + 3 * 2 - 1) # Python follows typical mathmatical order of operations

# We looked at strings, integers, and floats
'Hello' # This is a string
100 # This is an integer
100.5 # This is a float, notice the decimal point

# We looked at variables and including those variables in print commands
my_dogs = 0
print('I have', my_dogs, 'dogs')
type(my_dogs) # type is used for finding out the variable type

a = 5
print(a + a) # We can set integers and floats to variables and operate them
a = a + a
print(a + a)

# Of course, we can use integers and floats together
my_income = 100
tax_rate  = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)

# We can use 's or ""s for strings to help avoid syntax errors
"This isn't invalid syntax"

# We looked at indexing which starts at 0
indextest = 'Circus'
print(indextest[0])
print(indextest[-1]) # Negatives are used for right to left
print(indextest[0:4]) # This is a range
print(indextest[0:6:2]) # This is a range with the last number defining jump distance

# We looked at escape charcters
print("The \"largest\" pizza you have ever seen!") # The backspaces are used here to escape the function of the ""s
print("THE\nLARGEST\nPIZZA\nEVER") # \n is used for new lines
print('The...\n\tWorld...\n\t\tSleeps...') # \t is used for tabbing

# We looked at how to determine string length
len('GitHub')

# We looked at concatenation
liquid = 'Sea'
drink = 'T' + liquid[1:3] 
print(drink)

meat = 'Ham'
filling = 'J' + meat[-2:3] # It should be of note, I can't end the range with -1 as this the character it stops before
print(filling)

# We can actually use maths on strings in certain cases
letter = 'z'
print(letter * 10)

'2' + '6' # Would give '26' in this case a string, strings will be concatenated and not treated like numbers

# We looked at functions
print('Adam'.upper()) # Having brackets after the function is important

x = "And we're just suppose to follow you?"
print(x.split()) # This will split the variable string contents into a list
print(x.split('e')) # This will split the variable using the letter 'e' rather than spaces

# Strings are immutable
""" 
x = 'Hello'
x[0] = 'M' # This cant be changed in this way
print(x)
""" # """s can be used for multi line comments, a good way to block out code

# We can insert functions into strings using {}s
print('The {} {} {}'.format('fox','brown','quick'))
print('The {2} {1} {0}'.format('fox','brown','quick')) # We can use numbers for ordering starting with 0
print('The {q} {b} {f}'.format(f='fox', b='brown',q='quick')) # We can assign variables inside the brackets of the function

result = 829
print("The result was {}".format(result)) # We can call outside variables
print("The result was {r}".format(r = result)) # We can have variables of our variables in functions

# Float formatting follows "{value:width.precision f}"
result = 829/1000 * 100
print("The result was {r}".format(r = result))
print("The result was {r:1.1f}".format(r = result))

# There is a newer method using fstrings
name = 'Mobius'
rank_number = 118
print (f'{name} is number {rank_number}.') # The integer was allowed in the string

# Another weird way of doing it
'Python %s!' %'rules' # Seems to be a less desirable method of inserting a string

# We looked at lists
my_list = [1,2,3]
my_list = ['STRING',100,26.5] # We can have multiple object types in a list
len(my_list) # Gives us the amount of items
my_list[0] # Calls an item

my_list = ['one', 'two', 'three']
another_list = ['four', 'five']
new_list = my_list + another_list # We can concatenate lists
print(new_list)

new_list[0] = 'ONE' # We can mutate a list unlike a string

new_list.append('six') # Used for appending a list
print(new_list)

new_list.pop() # Pops out the last number as output
popped_item = new_list.pop() # Thus we can use it as a variable input
print(popped_item)

new_list.pop(0) # We can pop out using positions

# We looked at how to sort lists and None types

num_list = [5,2,7,3,9,1,3,4,6,8]
num_list.sort() # Provides no output so can't be used as a variable
sorted_list = new_list.sort()
print(sorted_list) # This will print 'None'
print(num_list) # This however is sorted

num_list.reverse() # This does a reverse sort
print(num_list)