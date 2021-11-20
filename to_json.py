import functools
import json 

def to_json(func_to_decor):
    @functools.wraps(func_to_decor)
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        out = func_to_decor(*args, **kwargs)
        return json.dumps(out)
    return a_wrapper_accepting_arbitrary_arguments
