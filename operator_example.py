
from random import shuffle

from random import randint

mylist = [1, 2, 3]
for num in range(0, 11, 2):
    print(num)

index_count = 0
word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    (print('\n'))

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

for item in zip(mylist1, mylist2, mylist3):
    print(item)

print(list(zip(mylist1, mylist2, mylist3)))

mylist4 = [10, 20, 30, 40, 100]
print(min(mylist4))

mylist4 = [10, 20, 30, 40, 100]
print(max(mylist4))

mylist5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist5)
print(mylist5)


print(randint(0, 100))

results = float(input('Enter a number here: '))
print(results)



