def func_counter(func1):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func1(*args, **kwargs)
    wrapper.counter = 0
    return wrapper
