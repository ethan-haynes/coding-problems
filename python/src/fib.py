import time

def fib(n):
    if n == 0 or n == 1: return n
    return fib(n-1) + fib(n-2)

def mem_fib(n):
    memo = {}
    def __fib(n):
        if n in memo: return memo[n]
        if n <= 2: f = 1
        else: f = __fib(n-1) + __fib(n-2)
        memo[n] = f
        return f
    return __fib(n)

start_time = time.time()
print(fib(30), "non-mem version")
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(mem_fib(30), "mem version")
print("--- %s seconds ---" % (time.time() - start_time))
