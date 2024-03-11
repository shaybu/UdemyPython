def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Shay', 'Eve', 'Sally']
print(list(map(splicer, names)))


def check_even(num):
    return num % 2 == 0


mynum = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, mynum)))

print(list(map(lambda num: num ** 2, mynum)))

print(list(filter(lambda num: num % 2 == 0, mynum)))

print(list(map(lambda x: x[0], names)))

print(list(map(lambda x: x[::-1], names)))

