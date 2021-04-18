import time
import sys


def Combinations(products, promotions, customers):
    for product in range(products):
        for promotion in range(promotions):
            for customer in range(customers):
                yield(f"{product} - {promotion} - {customer}")


start_time = time.perf_counter()
for i in Combinations(5, 10, 20):
    print(i)

generator = Combinations(5, 10, 20)
execution_time = time.perf_counter() - start_time
print(execution_time)
print(sys.getsizeof(generator)/(1024*1024), "MB")