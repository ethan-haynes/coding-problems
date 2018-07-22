def tower_of_hanoi(towers):
    t1, t2, t3 = towers
    def move(n, source, target, auxiliary):
        if n > 0:
            move(n - 1, source, auxiliary, target)

            target.append(source.pop())

            move(n - 1, auxiliary, target, source)
    move(len(t1), t1, t3, t2)

towers = [[5,4,3,2,1],[],[]]
tower_of_hanoi(towers)
print(towers)
