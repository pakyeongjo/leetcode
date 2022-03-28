class Fibonacci:
    def solution_1(self, limit):
        fibonacci = []
        a, b = 0, 1
        while len(fibonacci) < limit:
            fibonacci.append(a)
            a, b = b, a + b
        return fibonacci[-1]

    def solution_2(self, limit):
        a, b = 0, 1
        while limit:
            yield a
            a, b = b, a + b
            limit -= 1
        return a

    def solution_3(self, n):
        a, b = 0, 1
        while n:
            a, b = b, a + b
            n -= 1

        s = str(a)
        return len(s)


def solution_2(limit):
    a, b = 0, 1
    while limit:
        yield a
        a, b = b, a + b
        limit -= 1
    return a


# fib = solution_2(10)
# next(fib)
# for item in fib:
#     print(item)
