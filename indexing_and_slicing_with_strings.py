#!/usr/bin/env python
# coding: utf-8

# In[2]:


mystring = "Hello World"
print(mystring)

print(mystring[0])

var = mystring[8]
print(mystring[8])

var1 = mystring[-2]
print(mystring[-2])

var2 = mystring[-3]

s = 'hello'
print('print out e using indexing', s[1])

s = 'hello'
print('Reverse the string using slicing', s[::-1])

# Given dictionary
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}

# Accessing 'hello' using keys and indexing
hello = d['k1'][2]['k2'][1]['tough'][2][0]

# Printing the result
print("The 'hello' value is:", hello)
