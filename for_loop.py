mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    print(num)

for num in mylist:
    # check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Numbers: {num}')

for num in mylist:
    # check for negative
    if num % 2 == 1:
        print(num)
    else:
        print(f'even numbers {num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum)

for letter in 'Hello World':
    print(letter)

tup = (1, 2, 3)
for item in tup:
    print(item)

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(mylist))

for item in mylist:
    print(item)

for a, b in mylist:
    print(b)

mylist = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]
for a, b, c in mylist:
    print(b, c)

d = {'k1': 1, 'k2': 2, "k3": 3}

for key, value in d.items():
    print(value)

# Looping through a dictionary
student_scores = {"John": 85, "Alice": 90, "Bob": 75}
for name, score in student_scores.items():
    print(f"{name}: {score}")

# Looping with enumerate()
fruits = ["apple", "banana", "orange", "grape"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Looping with zip()
names = ["John", "Alice", "Bob"]
scores = [85, 90, 75]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Looping with range() and step size
for i in range(0, 10, 2):
    print(i)





