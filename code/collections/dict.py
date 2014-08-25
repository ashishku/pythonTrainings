from pprint import pprint as pp

d1 = {"a": 1, "b": 2, "c": 3}

for key in d1:
    print(key, d1[key])

for value in d1.values():
    print(value)

for tuple in d1.items():
    print(tuple)

for key, value in d1.items():
    print(key, value)

pp(d1)