def doubler(func1):
    def wrapper():
        func1()
        func1()
    return wrapper
