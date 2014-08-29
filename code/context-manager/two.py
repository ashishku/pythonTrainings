from contextlib import contextmanager

@contextmanager
def my_other_context_manager():
    # __enter__
    print("Before body.")
    try:
        yield "My Context Manager"
        #__exit__ no exception
        print("After body. no exception")
    except:
        #__exit__ with exception
        print("After body. with exception")
    
if __name__ == '__main__':
    with my_other_context_manager() as mcm:
        print(mcm)
        print("No Execption in body")

    print("\n\n\n")

    with my_other_context_manager() as mcm:
        print(mcm)
        print("Execption in body")
        raise ValueError('Some Exception')
