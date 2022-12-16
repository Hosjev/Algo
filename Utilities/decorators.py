"""Place for custom decorators"""
import functools
import time
import random

PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


def simp_deco(func):
    @functools.wraps(func)
    def wrapper_simp(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper_simp


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


def repeat(_func=None, *, num_times=1):
    """Arg taken (or not) to repeat function"""
    def dec_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for n in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    if not _func:
        return dec_repeat
    return dec_repeat(_func)


def timer(func):
    """Print the runtime of the decorated function"""
    #Replace with TIMEIT function?
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:2.4f} secs")
        return value
    return wrapper_timer


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__!r} with combined args: ({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


def dec_pa(func):
    """Returns pure wrapper:Execute func then return value"""
    @functools.wraps(func)
    def wrap_pa(*args, **kwargs):
        value = func(*args, **kwargs)
        return value
    return wrap_pa


def slow_down(_func=None, *, rate=1):
    """
    Sleep {rate} second before calling the function

    Since the function to decorate is only passed in directly
    if the decorator is called without arguments, the function
    must be an optional argument. This means that the decorator
    arguments must all be specified by keyword. You can enforce
    this with the special * syntax, which means that all following
    parameters are keyword-only.

    Arguments:
        _func: <function> present IF decorator used w/args
            *: <see above>
         rate: <int> how many seconds we wait
    Returns:
        An inner or outer wrapper.
    """
    def dec_slow_wrap(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down

    #If function called with addtl args(rate), None
    if _func is None:
        return dec_slow_wrap
    else:
        return dec_slow_wrap(_func)


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


def cache(func):
    """Keep a cache of previous function calls.
    Instead use functools.lru_cache(maxsize=num)"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        print(f"Wrapper dict: {wrapper_cache.cache[cache_key]} - {func.__name__}")
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


class CountCalls:
    """Class to count function/method calls"""
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call to {self.func.__name__!r} at {self.count}")
        value = self.func(*args, **kwargs)
        return value
