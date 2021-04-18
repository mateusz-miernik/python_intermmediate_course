import random


# def random_with_sum(number_of_tastes, number_of_trials, asserted_sum):
#     trial = 0
#     numbers = []
#
#     while True:
#         trial += 1
#         for num in range(number_of_tastes):
#             x = random.randrange(1, asserted_sum)
#             asserted_sum -= x
#             numbers.append(x)
#         yield (trial, numbers)


def random_with_sum(number_of_tastes, asserted_sum):
    trial = 0
    numbers = []

    while True:
        trial += 1
        for num in range(number_of_tastes):
            x = random.randint(1, 100)
            numbers.append(x)
        if sum(numbers) == asserted_sum:
            yield((trial, numbers))
            trial = 0
        numbers.clear()


for i in range(10):
    result = random_with_sum(3, 100)
    (number_of_trials, numbers) = next(result)
    print(number_of_trials, numbers)

#############################################################

# def random_with_sum(number_of_values, asserted_sum):
#     trial = 0
#     numbers = list(range(number_of_values))
#     while True:
#
#         trial += 1
#         for i in range(number_of_values):
#             numbers[i] = random.randint(1, 101)
#
#         if sum(numbers) == asserted_sum:
#             yield ((trial, numbers))
#             trial = 0
#
#
# for i in range(10):
#     (number_of_trials, numbers) = next(random_with_sum(3, 100))
#     print(number_of_trials, numbers)
