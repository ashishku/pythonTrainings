a_var = 1

def a_func():
    a_var = a_var + 1
    print(a_var, '[ a_var inside a_func() ]')

print(a_var, '[ a_var outside a_func() ]')
a_func()
print(a_var, '[2 a_var outside a_func() ]')