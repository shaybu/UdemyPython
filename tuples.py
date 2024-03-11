# Type list vs type tuples
t = (1, 2, 3)
mylist = []
print(type(mylist))
print(type(t))
print(len(t))

t = ('one', 2)
print(t)

print(t[0])
print(t[1])

t = ('a', 'a', 'b')
print(t.count('a'))
print(t.count('b'))
print(t.index('b'))
print(t.index('a'))

# Tuple with Different Data Types
tup1 = (1, 'Hello', 3.14)
print(tup1)

# Nested Tuple
tup2 = ('apple', [1, 2, 3], ('blue', 'green'))
print(tup2)

# Tuple of numbers
tuple1 = (1, 2, 3, 4, 5)

# Printing the tuple
print("Tuple of Numbers:", tuple1)

# Accessing elements by index
print("Element at index 2:", tuple1[2])

# Length of the tuple
print("Length of the tuple:", len(tuple1))

# Tuple of strings
tuple2 = ("apple", "banana", "orange")

# Printing the tuple
print("Tuple of Strings:", tuple2)

# Concatenating tuples
tuple3 = tuple2 + ("grape", "pineapple")
print("Concatenated Tuple:", tuple3)


# Tuple of mixed data types
tuple3 = (1, "apple", 3.14, True, "banana")

# Printing the tuple
print("Mixed Tuple:", tuple3)

# Slicing the tuple
sliced_tuple = tuple3[1:4]
print("Sliced Tuple:", sliced_tuple)

# Tuple packing
tuple4 = 1, 2, 3
print("Packed Tuple:", tuple4)

# Tuple unpacking
a, b, c = tuple4
print("Unpacked Tuple:", a, b, c)








