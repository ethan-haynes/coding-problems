def paint_fill(m, point, color):
    x,y = point
    current_color, memo = m[y][x], set()
    
    def fill(x,y):
        k = f'{x}{y}'
        if k not in memo: # check if we have already traversed this direction
            memo.add(k)
            if m[y][x] == current_color:
                m[y][x] = color
               
                # try left, right, up, down
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
