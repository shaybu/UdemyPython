def say_hello():
    print('hello')


def say_hello1(name='Default'):
    print(f'hello {name}')


say_hello1()


def add_num(num1, num2):
    return num1 + num2


def even_check(number):
    return number % 2 == 0


print(even_check(20))


def check_even_list(num_list):
    # return all the even numbers in the list

    # placeholder variables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


print(check_even_list([2, 6, 3]))

stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for ticker, price in stock_prices:
    print(price + (0.1 * price))

work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_the_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass
    return employee_of_the_month, current_max


print(employee_check(work_hours))
