from functools import reduce

def D(n):
    if n == 0:
        return 1
    elif n == 1:
        return n**n
    
    return D(n, D(n, n-1, n), n-1)

def F(n):
    x = n
    y = 0
    
    while True:
        if x % 2 == 0:
            x = x / 2
        else:
            x = D(x)*D(3) + 1
            y = y + n/(y+1)

        if y > n:
            return x

def G(n):
    return reduce(lambda val, _: F(val*val), range(n), n)

def H(n):
    return reduce(lambda val, _: G(val*val), range(n), n)

def J(n):
    return reduce(lambda val, _: H(val*val), range(n), n)

print(J(J(13)))
