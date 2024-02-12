
# cheese += 'Oke' attempts to concatenate a string 'Oke' to a list cheese. This operation is not valid for lists
# in Python.
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 'Oke']

cheese += ['Oke']
#  Add the string 'Oke' as a single-item list. Enclosing 'Oke' in square brackets to create a list with one element.

# To add 'Oke' to the end of the cheese list, you can use the append() method:

cheese.append('Oke')

print(cheese)

# the extend() method adds two new cheeses to the list with a single command,
# it takes an iterable (such as a list) and adds each element of that iterable to the list:

cheese.extend(['Gouda', 'Edam'])

