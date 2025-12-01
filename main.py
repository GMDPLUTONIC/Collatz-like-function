from functools import reduce

def D(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n ** D(D(D(D(D(n-1)) - 1)))

def F(n):
    x = n
    y = 0
    
    while True:
        if x % 2 == 0:
            x = x / 2
        else:
            x = D(x)**D(3) + 1
            y = y + n/(y+2)

        if y > n:
            return x

def G(n):
    return reduce(lambda val, _: F(F(val)), range(n), n)

def H(n):
    return reduce(lambda val, _: G(G(val)), range(n), n)

def J(n):
    return reduce(lambda val, _: H(H(val)), range(n), n)

def K(n):
    return reduce(lambda val, _: J(J(val)), range(n), n)

print(K(K(K(K(K(K(99)))))))
