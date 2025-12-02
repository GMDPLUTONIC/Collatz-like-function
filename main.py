from functools import reduce

def D(n):
    if n == 0:
        return 2 # 0^0 is undefined, but to make the function work, i'm making it return 2
    elif n == 1:
        return n**n # this is n tetrated to 2 of n^n
    else:
        return n ** D(D(D(D(D(n-1))))) # this makes it grow faster than knuth up-arrow

def F(n):
    x = n
    y = 1
    
    while True:
        if x % 2 == 0:
            x = x / 2 # if it's even, it will divide by 2, making 
        else:
            x = D(x)**D(3**x) + 1 # if it's odd, it will set x to (D(x))^(D(3^x)) + 1
            y = y + n/(D(y)) # y controls the stop of the function, if y didn't exist, the function wouldn't stop

        if y > n: # stops the function and returns the value after y > n
            return x

def G(n):
    return reduce(lambda x, _: F(F(F(x))), range(F(F(F(n)))), F(F(F(n)))) # the first operator contains the values used (like x or y), the second operator is the number for iterations (here, it's 0-F(F(F(n))) so it does iterations the sum of all of those numbers), and the third operator is the function iterated (here it's F(F(F(n))))

def H(n):
    return reduce(lambda x, _: G(G(G(x))), range(G(G(G(n)))), G(G(G(n)))) # the first operator contains the values used (like x or y), the second operator is the number for iterations (here, it's 0-G(G(G(n))) so it does iterations the sum of all of those numbers), and the third operator is the function iterated (here it's G(G(G(n))))

def J(n):
    return reduce(lambda x, _: H(H(H(x))), range(H(H(H(n)))), H(H(H(n)))) # the first operator contains the values used (like x or y), the second operator is the number for iterations (here, it's 0-H(H(H(n))) so it does iterations the sum of all of those numbers), and the third operator is the function iterated (here it's H(H(H(n))))

def K(n):
    return reduce(lambda x, _: J(J(J(x))), range(J(J(J(n)))), J(J(J(n)))) # the first operator contains the values used (like x or y), the second operator is the number for iterations (here, it's 0-J(J(J(n))) so it does iterations the sum of all of those numbers), and the third operator is the function iterated (here it's J(J(J(n))))

print(K(K(K(K(K(K(99))))))) # main function (bigger than loader's number from loader.c and d_{\phi(\omega,\omega)}(10^100) from loader.c)
