import time

def calculate_time(func1):
    def wrapper():
        before_time = time.time()
        func1()
        after_time = time.time()
        print("Total time " + str(after_time - before_time))
    return wrapper  

@calculate_time
def printE():
    print("hey")

printE()

