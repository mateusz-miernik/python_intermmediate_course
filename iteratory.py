import datetime as dt
import sys

aTuple = (1,2,3,4,5)

it = iter(aTuple)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


class MilionDays:
    def __init__(self, year, month, day, maxdays):
        self.date = dt.datetime(year, month, day)
        self.maxdays = maxdays

    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration()
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1
        return ret

    def __iter__(self):
        return self


class OneDay(MilionDays):
    def __init__(self, year, month, day, maxdays):
        super().__init__(year, month, day, maxdays)
        self.day = day


md = MilionDays(2000, 1, 1, 2500000)
oneday = OneDay(2000, 1, 1, 2500000)
print(OneDay.__mro__)
# print(next(md))
# print(next(md))
# print(next(md))
print(sys.getsizeof(md)/1024)
for d in md:
    pass
