import re

st = 'Print only the words that start with s in this sentence'

# Split the string into words
words = st.split()

# Loop via each word
for word in words:
    # check if the word start with 's'
    if word.lower()[0] == 's':
        print(word)

# Use range() to print all the even numbers from 0 to 10.
for num in range(0, 11, 2):
    print(num)

print(list(range(0, 11, 2)))

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
divisible_by_3 = [num for num in range(1, 51) if num % 3 == 0]

# Printing the list
print(divisible_by_3)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

# Split the string into words
words = st.split()

# Iterate over each word
for word in words:
    # Check if the length of the word is even
    if len(word) % 2 == 0:
        print(f'"{word}" has an even number of letters')

print('\n')

st = 'Print every word in this sentence that has an even number of letters'
even_length_words = [word for word in st.split() if len(word) % 2 == 0]
for word in even_length_words:
    print(f'{word} has an even number of letters')

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

print('\n', '\n')

# Another way
# List comprehension to generate Fizz, Buzz, and FizzBuzz strings
result = [
    "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else
    "Fizz" if num % 3 == 0 else
    "Buzz" if num % 5 == 0 else
    str(num)  # Convert number to string if not divisible by 3 or 5
    for num in range(1, 101)
]

# Joining the elements of the result list with newline characters
output = "\n".join(result)

# Printing the output
print(output)


# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

first_letter = [word[0] for word in st.split()]
print(first_letter)
