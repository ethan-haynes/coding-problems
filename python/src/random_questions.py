import os 

def rev(s):
    out = ''
    for i in range(len(s)-1,-1,-1):
        out += s[i]
    return out

def fib(n, memo=None):
    if memo == None: memo = {}

    if n in memo: 
        f = memo[n]
    else:
        if n < 2: f = 1
        else: f = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = f
    return f

def multi_table():
    for i in range(1,13):
        s = ''
        for j in range(1,13):
            s = f'{s} {i * j}'
        print(s)

def r_file(path):
    num_file = open(path,'r')
    s = 0
    for num in num_file.readlines():
        s += int( num.split('\n')[0] )
    num_file.close()
    print(s)

def print_odd():
    for i in range(1,100):
        if i % 2 != 0: print(i)

def find_largest(arr):
    lgst = None
    for i in arr:
        if lgst == None or lgst < i:
            lgst = i
    return lgst

def to_hex(rgb):
    r, g, b = rgb
    return f'{r:x}' + f'{g:x}' + f'{b:x}'

path = os.path.dirname(os.path.abspath(__file__))

print(rev('this is a string'))
print(fib(7))
multi_table()
r_file(path + '/text_files/nums.txt')
print_odd()
print(find_largest([10,2,4,5,6,11,12,44,55,-99]))
print(to_hex([245,155,95]))
