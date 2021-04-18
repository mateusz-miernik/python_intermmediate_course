import time
import functools


def wrapper_time(func):
    def wrapped_func(*args, **kwargs):
        start = time.perf_counter()
        print(10 * '+')
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(end)
        print(func.__name__)
        return result
    return wrapped_func


# @wrapper_time
def get_sequence(n):

    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2

        return v


fcn_a = wrapper_time(get_sequence)
print(fcn_a(18))
print(get_sequence(5))

########################


def wrapper_timee(func):
    def wrapped_func(*args, **kwargs):
        start = time.perf_counter()
        print(10 * '+')
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(end)
        print(func.__name__)
        return result
    return wrapped_func


@wrapper_time
def get_sequencee(n):

    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2

        return v


print(get_sequencee(20))