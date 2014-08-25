student = {'Ram', 'Shayam', 'Sita', 'Gita'}
math = {'Ram', 'Gita'}
physics = {'Ram', 'Shayam', 'Gita', 'Sita'}
chemsitry = {'Ram', 'Shayam'}
biology = {'Sita', 'Shayam'}
english = {'Shayam', 'Sita', 'Gita'}

print(student.issuperset(math))
print(student.issuperset(physics))
print(student.issuperset(chemsitry))
print(student.issuperset(biology))
print(student.issuperset(english))

print(math.issubset(student))
print(physics.issubset(student))
print(chemsitry.issubset(student))
print(biology.issubset(student))
print(english.issubset(student))

print(math.union(biology))

print(biology.intersection(english))

print(student.difference(biology))