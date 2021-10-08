class Recursion(RecursionError):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def recurse(*args, **kwargs):
    """
    Use this instead of function/method name to call
    """
    raise Recursion(*args, **kwargs)
        
def tail_recurse(func):
    """
    Decorate recursive tail function with this
    **essentially, running a new function everytime
    """
    def decorated(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Recursion as r:
                args = r.args
                kwargs = r.kwargs
                continue
    return decorated
