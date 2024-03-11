# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if
# one or both numbers are odd

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # Both numbers are even
        return min(a, b)
    else:
        # At least one number is odd
        return max(a, b)


# Test the function
result1 = lesser_of_two_evens(4, 6)
print("Result 1:", result1)  # Output: 4

result2 = lesser_of_two_evens(3, 7)
print("Result 2:", result2)  # Output:


# Write a function takes a two-word string and returns True if both words begin with same letter

def same_start_letter(string):
    # Split the string into words
    words = string.split()

    # Check if both words begin with the same letter
    return words[0][0].lower() == words[1][0].lower()


# Test the function
result1 = same_start_letter("hello world")
print("Result 1:", result1)

result2 = same_start_letter("apple Air")
print("Result 2:", result2)


# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1, n2):
    return n1 == 20 or n2 == 20 or n1 + n2 == 20


# Test the function
print(makes_twenty(10, 10))  # Output: True
print(makes_twenty(20, 0))  # Output: True
print(makes_twenty(5, 15))  # Output: True
print(makes_twenty(2, 3))  # Output: False


# Level 1 Problems

# Write a function that capitalizes the first and fourth letters of a name

def capitalize_letters(name):
    # Check if the name has at least 4 characters
    if len(name) >= 4:
        # Capitalize the first and fourth letters
        capitalized_name = name[:1].upper() + name[1:3] + name[3:4].upper() + name[4:]
        return capitalized_name
    else:
        # If the name has less than 4 characters, return the original name
        return name


# Test the function
print(capitalize_letters("python"))
print(capitalize_letters("java"))
print(capitalize_letters("GO"))


# Given a sentence, return a sentence with the words reversed

def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words into a sentence
    reversed_sentence = " ".join(reversed_words)

    return reversed_sentence


# Test the function
print(reverse_sentence("Hello world"))
print(reverse_sentence("Python is awsome"))


# Given an integer n, return True if n is within 10 of either 100 or 200

def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


# Test the function
print(near_hundred(90))
print(near_hundred(104))
print(near_hundred(150))


# Level 2 Problems

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


# Test the function
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


# Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result


# Test the function
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum
# exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds
# 21, return 'BUST'

def blackjack(a, b, c):
    total_sum = a + b + c

    if total_sum <= 21:
        return total_sum
    elif 11 in (a, b, c) and total_sum - 10 <= 21:
        return total_sum - 10
    else:
        return 'BUST'


# Test the function
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to
# the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    total_sum = 0
    skip_section = False

    for num in arr:
        if num == 6:
            skip_section = True
        elif num == 9 and skip_section:
            skip_section = False
        elif not skip_section:
            total_sum += num

    return total_sum


# Test the function
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


# CHALLENGING PROBLEMS

# Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    code = [0, 0, 7]
    index = 0

    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    return False


# Test the function
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


# Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(n):
    # Initialize a boolean list to mark numbers as prime or composite
    primes = [True] * (n + 1)
    count = 0

    # 0 and 1 are not prime numbers
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Count prime numbers
    for prime in primes:
        if prime:
            count += 1

    return count


# Test the function
print(count_primes(100))


# Write a function that takes in a single letter, and returns a 5x5 representation of that letter

def print_big(letter):
    patterns = {
        'a': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
        'b': ['**** ', '*   *', '**** ', '*   *', '**** '],
        'c': [' *** ', '*   *', '*    ', '*   *', ' *** '],
        'd': ['**** ', '*   *', '*   *', '*   *', '**** '],
        'e': ['*****', '*    ', '**** ', '*    ', '*****']
    }

    if letter.lower() in patterns:
        for line in patterns[letter.lower()]:
            print(line)
    else:
        print("Letter not found in dictionary")


# Test the function
print_big('b')
