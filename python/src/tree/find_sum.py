from make_btree import Tree, make_btree, traverse
t = make_btree([1,2,3,4,5,6,7]) # setup


# find all the paths that sum to target
def find_sum(tree, target):
    sums, path = [], []
    def walk(root, count=0, arr=[]):
        if root:
            arr.append(root.data)
            for i in range(len(arr)): path.append(arr[i:])
            walk(root.left, count+1, arr.copy())
            walk(root.right, count+1, arr.copy())
    walk(tree)
    for n in path:
        if sum(n) == target: sums.append(n)
    return sums

# print all the paths that sum to target
def print_sum(root, target, count=0, arr=[]):
    if root:
        arr.append(root.data)
        for i in range(len(arr)):
            if sum(arr[i:]) == target: print(arr[i:])
        print_sum(root.left, target, count+1, arr.copy())
        print_sum(root.right, target, count+1, arr.copy())


print('target: {t} result: {r}'.format(t=1, r=find_sum(t,1)))
print('target: {t} result: {r}'.format(t=2, r=find_sum(t,2)))
print('target: {t} result: {r}'.format(t=3, r=find_sum(t,3)))
print('target: {t} result: {r}'.format(t=4, r=find_sum(t,4)))
print('target: {t} result: {r}'.format(t=5, r=find_sum(t,5)))
print('target: {t} result: {r}'.format(t=6, r=find_sum(t,6)))
print('target: {t} result: {r}'.format(t=7, r=find_sum(t,7)))

print_sum(t,1)
print_sum(t,2)
print_sum(t,3)
print_sum(t,4)
print_sum(t,5)
print_sum(t,6)
print_sum(t,7)
