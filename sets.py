my_set = set()
print(my_set)

my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.remove(1)
print(my_set)

# Set of Numbers
numbers_sets = {1, 2, 3, 4, 5}
print('Set of Numbers:', numbers_sets)

# Set of strings
fruits_set = {"apple", "banana", "orange", "grape", "pineapple"}
print('set of Fruits:', fruits_set)

# Set of mixed data types
mixed_set = {10, "hello", 3.14, True}

# Printing the mixed set
print("Mixed Set:", mixed_set)

# Empty set
empty_set = set()

# Printing the empty set
print("Empty Set:", empty_set)

# Creating a frozenset
# After creating a frozenset, you cannot modify it
# Frozensets are useful in situations where you want to create a set of unique, immutable elements.
frozen = frozenset([1, 2, 3, 4, 5])
print(frozen)

# Set of numbers
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
print("Union of sets:", union_set)


# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# Difference between sets
difference_set = set1.difference(set2)
print("Difference between sets:", difference_set)

# Symmetric difference between sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference between sets:", symmetric_difference_set)

# Set of strings
set1 = {"apple", "banana", "orange", "grape", "pineapple"}

# Membership testing
print("Is 'banana' in the set?", "banana" in set1)
print("Is 'kiwi' in the set?", "kiwi" in set1)


# Set of mixed data types
set1 = {1, "apple", 3.14, True}

# Removing an element
set1.remove("apple")
print("Set after removing 'apple':", set1)


