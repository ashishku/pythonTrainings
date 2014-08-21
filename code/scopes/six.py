a_var = 'global value'

def outer():
    a_var = 'local value'
    print('outer before:', a_var)
    def inner():
        print('in inner():', a_var)
    inner()
    print("outer after:", a_var)


outer()