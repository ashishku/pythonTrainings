l1 = ["aaaa", "bb", "c", "ddd"]

l1.reverse()
print(l1)

l1.sort()
print(l1)

l1.sort(key=len)
print(l1)

l1.sort(key=len, reverse=True)
print(l1)

l2 = [[1, 2, 3], [4, 5, 6]]
print(l2)

l3 = l2.copy()
l4 = list(l3)

l2[1] += [7]

print(l2)
print(l3)
print(l4)