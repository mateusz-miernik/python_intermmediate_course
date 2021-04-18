import functools
import time


@functools.lru_cache(maxsize=100)
def fib(n):
    if n <=2:
        return n
    else:
        return fib(n-1) + fib(n-2)


start_main = time.time()
for i in range(38):
    start = time.time()
    print(fib(i))
    stop = time.time()
    print('Execution time is {}'.format(stop-start))

stop_main = time.time()
print('All execution time is {}'.format(stop_main-start_main))
print(fib.cache_info())