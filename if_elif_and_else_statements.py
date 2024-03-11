if True:
    print(f"It's True")

hungry = True
if hungry:
    print('FEED ME!')

hungry = False
if hungry:
    print('FEED ME!')
else:
    print('Im not hungry')

loc = 'Bank'
if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!')
else:
    print('I do not know much.')

name = 'Sammy'
if name == 'Frank':
    print('Hello Frank')
elif name == 'Sammy':
    print('Hello Sammy')
else:
    print('What is your name?')

# if-else statement
x = 3
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")


# if-elif-else statement
x = 10
if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is equal to 10")

# Nested if-else statement
x = 15
if x >= 10:
    if x <= 20:
        print("x is between 10 and 20")
    else:
        print("x is greater than 20")
else:
    print("x is less than 10")


