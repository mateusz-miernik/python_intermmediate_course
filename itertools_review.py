import itertools as it


def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


def check_if_has_dividers(x):
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False


result = get_factors(20)
print(result)

candidate_list = list(range(1, 10001))
filtered_list = it.filterfalse(lambda x: sum(get_factors(x)) != x, candidate_list)
# print(list(filtered_list))

for i in list(filtered_list):
    print('{} {}'.format(i, get_factors(i)))


# prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 100000)))
# print(prime_numbers[:10])

prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 100)
print(list(prime_numbers))