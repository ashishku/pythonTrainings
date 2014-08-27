from json import JSONEncoder

class JSONSerializer(JSONEncoder):
    def __init__(self, f):
        super().__init__()
        self.f = f
        
    def __call__(self, *args, **kwargs):
        x = self.f(*args, **kwargs)
        return self.encode(x)

@JSONSerializer
def get_some_data():
    my_dict = {"a": 1, "b": 2, "c": 3}
    return my_dict

@JSONSerializer
def get_some_more_data():
    my_list = [{"a": 1, "b": 2, "c": 3},
               {"x": 4, "y": 5, "z": 6}
               ]
    return my_list