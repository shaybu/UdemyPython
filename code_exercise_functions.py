# 17
def myfunc(*args):
    return sum(args)


# 18
def myfunc2(*args):
    even_numbers = []
    for number in args:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


#  19
def myfunc3(string):
    result = ''
    for i, char in enumerate(string):
        if i % 2 == 0:
            result += char.lower()
        else:
            result += char.upper()
    return result


# Test the function
input_string = "abcdefghijklmnopqrstuvwxyz"
output_string = myfunc3(input_string)
print(output_string)
