my_dict = {'key1': 'value1', 'key2': 'value2'}

print(my_dict)

print(my_dict['key1'])

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])
print(prices_lookup['oranges'])
print(prices_lookup['milk'])

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
print(d['k1'])
print(d['k2'])
print(d['k3']['insideKey'])

print(d['k2'][2])

d = {'key1': ['a', 'b', 'c', 'd']}
mylist = d['key1']
print(mylist)
letter = mylist[2]
print(letter.upper())

# d1 = {'key1': ['a', 'b', 'c', 'd']}
# print(d1[2].upper())


dict1 = {'v1': 100, 'v2': 200}
print(dict1)
dict1['v3'] = 300
print(dict1)

dict1['v1'] = 'NEW VALUE'
print(dict1)

k = {'v1': 100, 'v2': 200, 'v3': 300}
k.keys()
print(k)
print(k.items())


# Dictionary information about a student
student = {
    "name": "John Doe",
    "age": 20,
    "gender": "Male",
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

print("Student Information:")
for key, value in student.items():
    if isinstance(value, list):
        value = ", ".join(value)
    print(f"{key}: {value}")


# Dictionary information about a book
book = {
    "title": "Harry Potter",
    "author": "Rowling",
    "year": "1997",
    "genre": "Fantasy",
    "pages": 320
}

print("Book Information")
for key, value in book.items():
    print(f"{key}: {value}")
    # print(f"{key}: {value[1:]}")
    # print(f"{key}: {value[:2]}")


# Dictionary details of an employee with boolean.
employee = {
    "id": 12345,
    "name": "Alice Smith",
    "department": "Human Resources",
    "salary": 50000,
    "is_manager": False
}

print("Employee Details")
for key, value in employee.items():
    print(f"{key}: {value}")


# Dictionary information about a country, handling the case where the value is a list.
country = {
    "name": "United States",
    "population": 331000000,
    "capital": "Washington D.C.",
    "languages": ["English", "Spanish"],
    "currency": "US Dollar"
}

print("Country Information")
for key, value in country.items():
    print(f"f{key}:{value}")

# Dictionary details of a product, including a nested dictionary for specifications and printing them.
product = {
    "name": "Laptop",
    "brand": "HP",
    "price": 899.99,
    "in_stock": True,
    "specs": {
        "processor": "Intel Core i7",
        "RAM": "16GB",
        "storage": "512GB SSD"
    }
}
print("Product Information")
for key, value in product.items():
    if isinstance(value,dict):
        print(f"{key}:")
        for k, v in value.items():
            print(f" {k}: {v}")
    else:
        print(f"{key}: {value}")


