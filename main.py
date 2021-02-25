# Tuple items are enclosed in round brackets
# Tuple is ordered
# Tuple is immutable
# Tuple elements do not need to be unique
# Elements can be of different data types

'''
Creating a Tuple
'''

# # An empty Tuple
# tuple = ()
# # Tuple can hold heterogneous ( differend) data types
# tuple = ( 'Dog', [4,3,2,1], (1,2,3,4))
# tuple = 1234, 4321
# tuple = 'Hello world!', # if you have a single item it must followed by a comma in order to became a tuple instead a string.
# tuple = ('Hello,')
# print(tuple)

'''
Access Tuple Elements
'''
# # Accessing tuple elements by indexing
# tuple = (1234, 4321, 'Hello')
# # access with index
# print(tuple[0])
# # access with negative index
# print(tuple[-1])


'''
Slicing Tuple in Python
'''

# fruits = ('Orange', 'Apple', 'Pear', 'Grapes', 'Banana')

# print(fruits[:]) # beginning to end
# print(fruits[2:5]) # index 2nd to 5th items
# print(fruits[:-2]) # remove last two items or remove last item(s)
# print(fruits[:2]) # returns first 2 items
# print(fruits[2:]) # index 2 to the end
# print(fruits[::2]) # every nth(2 in this case) item
# print(fruits[::-1]) # Reverse list

'''
Changing a Tuple
'''

# fruits = ('Orange', 'Apple', 'Pear', 'Grapes', 'Banana', [4,3,2,] )

# fruits[0] = 'Pear' # immutable, item can't be changed and will get traceback.

# #Change mutable list inside a tuple.
# fruits[5][0] = 5 
# print(fruits)

'''
Deleting a Tuple
'''


# fruits = ('Orange', 'Apple', 'Pear', 'Grapes', 'Banana', [4,3,2,])

#C an't delete items
# del fruits[0]
# print(fruits)

# but we can delete the entire tuple
# del fruits
# print(fruits) 


'''
Tuple methods
'''

# Only has 2 built-in methods


fruits = ('Orange', 'Apple', 'Pear', 'Grapes', 'Banana', 'Orange', [4,3,2,] )

# print(dir(tuple))
print(fruits.count('Orange'))
print(fruits.index('Banana'))