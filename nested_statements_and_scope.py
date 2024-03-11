name = 'THIS IS A GLOBAL STRING'


def greet():
    # name = 'Sammy'

    def hello():
        print('Hello ' + name)

    hello()


greet()

y = 50


def func(y):

    print(f'y is {y}')

    y = 'new_value'
    print(f'I just global changed y to {y}')
    return y


print(y)
func(y)
