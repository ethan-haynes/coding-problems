def forsum(nums, target):
    s = []
    def permutations(head, tail=[]):
        if len(head) == 0: s.append(tail)
        else:
            for i in range(len(head)):
                permutations(head[0:i] + head[i+1:], tail + [head[i]])

    permutations(nums)
    return set(tuple(sorted(i[:4])) for i in s if sum(i[:4]) == target)

forsum([1, 0, -1, 0, -2, 2], 0)
