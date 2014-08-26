squares = (x*x for x in range(10))

for i in range(10):
    print(next(squares))

s = sum(x*x for x in range(10))
print("sum of sq: " + str(s))