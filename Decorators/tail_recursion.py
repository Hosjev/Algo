class Recursion(RecursionError):
    def __init__(self, *args, **kwargs):
        """ Thanks to C. Penner """
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
    **using:
          1) decorate function/method w/tail_recurse
          2) which simply returns the object execution
          3) return `recurse` instead of named function/method
          4) which raises 'Recursion' (catching RE)
          5) which sets variables to object
          6) when RE occurs, reset those variables and...
          7) continue as if function/method called 1st time
          8) stack is reset w/cPy defaults until limit reached
    """
    def decorated(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Recursion as r: # catch RE
                args = r.args      # build new object
                kwargs = r.kwargs  # build new object
                continue           # re-enter try block
    return decorated
