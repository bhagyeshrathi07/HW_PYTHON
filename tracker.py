def func_counter(func1):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func1(*args, **kwargs)
    wrapper.counter = 0
    return wrapper


@func_counter
def foo(y):
    return y+2**3-34

foo(6)
foo(5)
print(foo.counter)
