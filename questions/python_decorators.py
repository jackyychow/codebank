# Source: Akuna
# Question: Implement and explain Python decorators.
#

"""
Python decorators are a powerful and elegant way to modify or extend the behavior of functions or methods without directly altering their source code. 
They essentially wrap a function with another function, adding functionality before, after, or around the original function's execution. 
"""
import time
import functools

# def timeit(func):
#     """
#     A decorator to measure the execution time of a function.
#     """
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         total_time = end_time - start_time
#         print(f"Function '{func.__name__}' took {total_time:.4f} seconds to execute.")
#         return result
#     return wrapper

def timeit(func):
    def wrapper(*args, **kwargs):
        print(f"function {func.__name__} started")
        result=func(*args,**kwargs)
        print(f"function {func.__name__}  concluded")
        return result
    
    return wrapper

@timeit
def example_function(n):
    """
    An example function to demonstrate the timeit decorator.
    """
    sum_val = 0
    for i in range(n):
        sum_val += i
    return sum_val

# Using the decorated function
example_function(1000000)
example_function(5000000)


def mission_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time=time.perf_counter()
        print(f"Mission duration: {end_time - start_time} seconds")
        return result

    return wrapper

@mission_timer
def launch_probe(dest):
    time.sleep(1)
    return f"Launching probe into {dest}"

@mission_timer
def deploy_satellite(dest,speed):
    time.sleep(2)
    return f"Deploying satellite to {dest} at {speed}km/h"

launch_probe("Mars")
deploy_satellite("Sun", 800)
