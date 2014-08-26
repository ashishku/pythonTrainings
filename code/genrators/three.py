def fibonacci():
    fn1 = 1
    fn2 = 0
    yield fn2
    yield fn1
    while(True):
        (fn1, fn2) = (fn1 + fn2, fn1)
        yield fn1

fib = fibonacci()
for i in range(15):
    print(next(fib)) 