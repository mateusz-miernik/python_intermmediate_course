
def fib(number):
    n1, n2 = 0, 1
    for i in range(number):
        if i < number:
            print(n1)
            n = n1 + n2
            n1 = n2
            n2 = n


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)


def recur_fcn(n):
    idx = 0
    print(n)
    idx += 1
    if idx < n:
        return recur_fcn(n-1)
    else:
        return 0


fib(10)

for i in range(10):
    print(recur_fibo(i))


print(30*'%')
recur_fcn(100)