def head(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


h = head(3, [1, 2, 3, 4, 5, 6])
next(h)
next(h)
next(h)
next(h)