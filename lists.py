my_list = [1, 2, 3]
print(my_list)

my_list1 = ['STRING', 100, 32.2]

print(my_list1)
print(len(my_list1))

my_list2 = ['one', 'two', 'three']
print(my_list2[0])

print(my_list2[1:])

print(my_list2[2:])

another_list = ['four', 'five']

print(my_list2 + another_list)

new_list = my_list2 + another_list

print(new_list)

new_list[0] = 'ONE ALL CAPS'
print(new_list)

new_list.append('six')
print(new_list)

new_list.append('seven')
print(new_list)

new_list.pop()
print(new_list)

popped_item = new_list.pop()
print(popped_item)

new_list.pop(0)
print(new_list)

new_list.pop(-1)
print(new_list)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

my_sorted_list = new_list.sort()
print(new_list)

my_num_list = num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

new_list.reverse()
print(new_list)

# List of numbers:
numbers = [1, 2, 3, 4, 5]
print("List of numbers", numbers)

# List of strings
fruits = ["apple", "banana", "orange", "grape", "pineapple"]
print("List of fruits", fruits)

# List of mixed data types:
mixed_list = [10, "hello", 3.14, True]
print("Mixed list", mixed_list)

# List of lists (Nested List)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix")
for row in matrix:
    print(row)

empty_list = []
print("Empty list", empty_list)


# Sorted list
sorted_numbers = [5, 2, 8, 1, 3]
sorted_numbers.sort()
print("Sorted List of Numbers", sorted_numbers)

# Reversed Sorted list
reversed_numbers = [1, 2, 3, 4, 5]
reversed_numbers.reverse()
print("Reversed Sorted List of Numbers", reversed_numbers)

# Sorted list of strings
fruits = ["banana", "apple", "orange", "grape", "pineapple"]
sorted_fruits = sorted(fruits)
print("Sorted List of Fruits", sorted_fruits)

# Printing the sorted strings with their corresponding indices in the original list
print("Sorted List of Fruits with Indices:")
for index, fruit in enumerate(sorted_fruits):
    original_index = fruits.index(fruit)
    print(f"Index: {original_index}, Fruit: {fruit}")

# Printing the first index of the sorted list
fruits = ["banana", "apple", "orange", "grape", "pineapple"]
print("First index of the sorted list:", sorted_fruits[0])

# Slicing the first index of the sorted list
first_index_sliced = sorted_fruits[0][0:3]  # Slicing the first three characters
print("Sliced value of the first index:", first_index_sliced)


mystring = 'hello'
myslist = []
for letter in mystring:
    myslist.append(letter)
    print(myslist)

my_list = [letter for letter in mystring]
print(myslist)

myslist = [x for x in 'word']
print(myslist)

myslist = [num**2 for num in range(0, 11)]
print(myslist)





