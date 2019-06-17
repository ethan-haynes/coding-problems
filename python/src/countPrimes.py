def countPrimes(N: int) -> int:
    c = 0
    cache = [True] * N
    cache[0] = cache[1] = False
    
    for n in range(2, N):
        if cache[n]:
            c += 1
            for i in range(n*2, N, n):
                cache[i] = False
    return c


def countPrimesTwo(N: int) -> int:
    
    def isPrime(n: int) -> bool:
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True
    
    c = 0
    for n in range(2,N):
        if isPrime(n): c += 1

    return c

print(countPrimes(10))
print(countPrimesTwo(10))
