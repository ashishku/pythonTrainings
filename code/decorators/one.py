from json import JSONEncoder

def serialize_to_json(f):
    json_encoder = JSONEncoder()
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return json_encoder.encode(x)
    return wrap

@serialize_to_json
def get_some_data():
    my_dict = {"a": 1, "b": 2, "c": 3}
    return my_dict

@serialize_to_json
def get_some_more_data():
    my_list = [{"a": 1, "b": 2, "c": 3},
               {"x": 4, "y": 5, "z": 6}
               ]
    return my_list