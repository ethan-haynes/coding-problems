def paint_fill(m, point, color):
    memo = set()
    x,y = point
    current_color = m[y][x]
    def fill(x,y):
        k = f'{x}{y}'
        if k not in memo:
            memo.add(k)
            if m[y][x] == current_color:
                m[y][x] = color
                
                if 0 <= x-1: fill(x-1,y)
                if x+1 <= len(m[y])-1: fill(x+1,y)
                if 0 <= y-1: fill(x,y-1)
                if y+1 <= len(m)-1: fill(x,y+1)
                
    fill(x,y)

m = [
        [1,0,0],
        [0,1,0],
        [0,0,0]
    ]

for i in range(len(m)):
    print(m[i])

print('-------------------------------')

paint_fill(m,[2,2],2)

for i in range(len(m)):
    print(m[i])

m = [
        [1,0,0,0,0,0],
        [0,1,0,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,1,0,0],
        [0,0,0,0,1,0],
        [0,0,0,0,0,1]
    ]

print('-------------------------------')

for i in range(len(m)):
    print(m[i])

print('-------------------------------')

paint_fill(m,[2,2],2)

for i in range(len(m)):
    print(m[i])
    

print('-------------------------------')

paint_fill(m,[0,5],3)

for i in range(len(m)):
    print(m[i])
