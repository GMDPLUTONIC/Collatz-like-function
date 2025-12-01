from functools import reduce

def D(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n** D(n** D(n-1)**n) **n

def F(n):
    x = n
    y = 0
    
    while True:
        if x % 2 == 0:
            x = x // 2
        else:
            x = D(x)*D(3) + 1
            y = y + n/(y+2)

        if y > n:
            return x

def G(n):
    return reduce(lambda val, _: F(D(val)), range(n), n)

def H(n):
    return reduce(lambda val, _: G(D(val)), range(n), n)

def J(n):
    return reduce(lambda val, _: H(D(val)), range(n), n)

print(J(J(J(J(99)))))
