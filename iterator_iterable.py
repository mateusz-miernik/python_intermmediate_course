import time
import sys


class CombinationsIterator:
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0
        # self.max_items = len(products)*len(promotions)*len(customers)

    def __next__(self):
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration()

        item_to_return = f"{self.current_product} - {self.current_promotion} - {self.current_customer}"
        self.current_customer += 1
        return item_to_return


class Combinations:
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.iterator = CombinationsIterator(self.products, self.promotions, self.customers)

    # def __getitem__(self, item):
    #     if item >= self.max_items:
    #         raise StopIteration()
    #     else:
    #         pos_products = item // (len(self.promotions)*len(self.customers))
    #         item = item % (len(self.promotions)*len(self.customers))
    #         pos_promotions = item // len(self.customers)
    #         item = item % len(self.customers)
    #         pos_customers = item
    #     return f"{self.products[pos_products]} - {self.promotions[pos_promotions]} - {self.customers[pos_customers]}"

    def __iter__(self):
        return self.iterator


start_time = time.perf_counter()

products = ["Product {}".format(i) for i in range(1, 50)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 5)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 50)]
print(customers)

combinations = Combinations(products, promotions, customers)

# for i in range(1, 30):
#     # here an analysis will be done - currently, just nothing happens :)
#     print(i)
#     print(combinations[i])


print(30*'%')
print('Going through object by for loop')
for c in combinations:
    # print(c)
    pass

print('Iterating of object by next function')
it = iter(combinations)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

execution_time = time.perf_counter() - start_time
print(execution_time)
print(sys.getsizeof(combinations)/(1024*1024), "MB")
# time.sleep(10)