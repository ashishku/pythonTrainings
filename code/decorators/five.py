import functools
from json import JSONEncoder

class JSONSerializer(JSONEncoder):
    def __init__(self, serialize = False):
        super().__init__()
        self._serialize = serialize
        
    def __call__(self, f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            x = f(*args, **kwargs)
            return self.encode(x) if self._serialize else x
        return wrap

def wrap_in_response(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        response = dict()
        try:
            x = f(*args, **kwargs)
        except ValueError as err:
            response["success"] = False
            response["message"] = str(err)
        else:
            response["success"] = True
            response["data"] = x
        return response
    return wrap

@JSONSerializer()
@wrap_in_response
def get_some_data(someBool=False):
    if someBool:
        raise ValueError("You passed true")
    my_dict = {"a": 1, "b": 2, "c": 3}
    return my_dict

@JSONSerializer(True)
@wrap_in_response
def get_some_more_data(someBool=False):
    if someBool:
        raise ValueError("You didn't pass false")
    my_list = [{"a": 1, "b": 2, "c": 3},
               {"x": 4, "y": 5, "z": 6}
               ]
    return my_list