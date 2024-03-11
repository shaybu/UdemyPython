print('This is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('fox', 'brown', 'quick'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))

results = 100 / 777
print("The results was {}".format(results))

print("The results was {r}".format(r=results))

print("The results was {r:1.5f}".format(r=results))

name = "Jose"
print(f'Hello, his name is {name}')

name = "Sam"
age = 3
print(f"{name} is {age} years old")
