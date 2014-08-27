from json import JSONEncoder

class JSONSerializer(JSONEncoder):
    def __init__(self, serialize = False):
        super().__init__()
        self._serialize = serialize
        
    def __call__(self, f):
        def wrap(*args, **kwargs):
            x = f(*args, **kwargs)
            return self.encode(x) if self._serialize else x
        return wrap

@JSONSerializer()
def get_some_data():
    my_dict = {"a": 1, "b": 2, "c": 3}
    return my_dict

@JSONSerializer(True)
def get_some_more_data():
    my_list = [{"a": 1, "b": 2, "c": 3},
               {"x": 4, "y": 5, "z": 6}
               ]
    return my_list