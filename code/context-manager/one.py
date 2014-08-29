class MyContextManager:
    def __enter__(self):
        print("Before body.")
        return "My Context Manager"
        
    def __exit__(self, exc_type, exec_val, exc_tb):
        print("After body. {}, {}, {}".format(exc_type, exec_val, exc_tb))   
        return True

if __name__ == '__main__':
    with MyContextManager() as mcm:
        print(mcm)
        print("No Execption in body")

    print("\n\n\n")

    with MyContextManager() as mcm:
        print(mcm)
        print("Execption in body")
        raise ValueError('Some Exception')
