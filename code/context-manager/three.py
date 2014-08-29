class MyContextManager:
    def __enter__(self):
        print("MyContextManager: Before body.")
        return "MyContextManager: My Context Manager"
        
    def __exit__(self, exc_type, exec_val, exc_tb):
        print("MyContextManager: After body. {}, {}, {}".format(exc_type, exec_val, exc_tb))   

from contextlib import contextmanager
@contextmanager
def my_other_context_manager():
    # __enter__
    print("my_other_context_manager: Before body.")
    try:
        yield "my_other_context_manager: My Context Manager"
        #__exit__ no exception
        print("my_other_context_manager: After body. no exception")
    except:
        #__exit__ with exception
        print("my_other_context_manager:  After body. with exception")
        raise
    
if __name__ == '__main__':
    with MyContextManager() as cm1, my_other_context_manager() as cm2:
        print(cm1)
        print(cm2)
        print("No Execption in body")

    print("\n\n\n")

    with MyContextManager() as cm1:
        with my_other_context_manager() as cm2:
            print(cm1)
            print(cm2)
            print("Execption in body")
            raise ValueError('Some Exception')