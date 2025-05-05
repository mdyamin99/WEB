import math
import time
def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        print('Started')
        func(*args, **kwargs)
        print('Ended')
        end = time.time()
        print(f'total time raken: {end-start}')
    return inner

# timer()()

@timer
def get_factorial(n):
    print('Factorial starting')
    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')

get_factorial(5)