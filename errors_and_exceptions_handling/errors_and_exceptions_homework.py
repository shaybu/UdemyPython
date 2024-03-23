try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("Type Error")

try:
    x = 5
    y = 0

    z = x / y
except:
    print("Type Error zero division")
finally:
    print("All Done")


def ask():
    waiting = True
    while waiting:
        try:
            n = int(input("Enter a number"))
        except:
            print("Please try again! \n")
            continue
        else:
            waiting = False

    print("Your number squared is: ")
    print(n ** 2)


ask()
