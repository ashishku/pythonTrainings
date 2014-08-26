def gen():
    print('return 1')
    yield 1
    print('return 2')
    yield 2
    print('return 3')
    yield 3
    print('return 4')
    yield 4


g = gen()
next(g)
next(g)
next(g)
next(g)
next(g)