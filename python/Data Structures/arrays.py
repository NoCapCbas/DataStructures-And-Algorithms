# arrays.py 

array_example = [1, 2, 3, 4, 5]

print(f'Array example: {array_example}'})

# Adding elements
array_example.append(6)

print(f'Adding element: {array_example}')

# Accessing elements 
print(f'Element at index 5: {array_example[5]}')

# Removing elements
removed_element = array_example.pop(1)

print(f'Element removed: {removed_element}')

# Modifying elements 
array_example[0] = 2 

print(f'Modified element at index 0: {array_example}')
