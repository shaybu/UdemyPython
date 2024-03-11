# Write a function that computes the volume of a sphere given its radius.
def sphere_volume(radius):
    pi = 3.14159
    volume = (4 / 3) * pi * (radius ** 3)
    return volume


# Test the function
radius = 2
print("Volume of the sphere with radius", radius, "is:", sphere_volume(radius))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def in_range(number, low, high):
    return low <= number <= high


# Test the function
num = 10
low_num = 5
high_num = 15
print(f"Is {num} in the range [{low_num}, {high_num}]? {in_range(num, low_num, high_num)}")

num = 20
print(f"Is {num} in the range [{low_num}, {high_num}]? {in_range(num, low_num, high_num)}")


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count


# Test the function
sample_string = 'Hello Mr. Rogers, how are you this fine Tuesday?'
upper_count, lower_count = count_upper_lower(sample_string)
print("No. of Upper case characters :", upper_count)
print("No. of Lower case characters :", lower_count)


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_elements(input_list):
    # Convert the list to a set to remove duplicates, then convert back to a list
    return list(set(input_list))


# Test the function
original_list = [1, 2, 3, 3, 4, 5, 5, 6, 6, 7]
unique_list = unique_elements(original_list)
print("Original List:", original_list)
print("Unique List:", unique_list)


# Write a Python function to multiply all the numbers in a list.

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


# Test the function
numbers = [1, 2, 3, 4, -5]
print("The sum of all numbers in the list is:", multiply_list(numbers))


# Write a Python function that checks whether a word or phrase is palindrome or not

def is_palindrome(word):
    # Convert the word to lowercase and remove spaces
    word = word.lower().replace(" ", "")

    # Compare the word with its reverse
    return word == word[::-1]


# Test the function
word1 = "radar"
word2 = "A man a plan a canal Panama"
word3 = "hello"

print(f"'{word1}' is a palindrome:", is_palindrome(word1))
print(f"'{word2}' is a palindrome:", is_palindrome(word2))
print(f"'{word3}' is a palindrome:", is_palindrome(word3))


# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any
# punctuation)

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in sentence.lower():
            return False
    return True


# Test the function
sentence1 = "The quick brown fox jumps over the lazy dog"
sentence2 = "Pack my box with five dozen liquor jugs"
sentence3 = "Hello world"

print(f"'{sentence1}' is a pangram:", is_pangram(sentence1))
print(f"'{sentence2}' is a pangram:", is_pangram(sentence2))
print(f"'{sentence3}' is a pangram:", is_pangram(sentence3))
