mas = []


def foo(b):
    if b == 0:
        return mas
    dig = b % 10
    mas.append(dig)
    foo(b // 10)


n = 170845

foo(n)
print(sum(mas))
