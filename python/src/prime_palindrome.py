import math
def isPrime(N: int) -> bool:
    for i in range(2,int(math.sqrt(N))+1):
        _, d = (N/i).as_integer_ratio()
        if d == 1: return False
    return True
        
        
def primePalindrome(N: int) -> int:
    for i in range(N, 10**8):
        if isPrime(i):
            p = str(i)
            if p == p[::-1]:
                return i
            
print(primePalindrome(6))
