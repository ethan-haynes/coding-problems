def find_sum(root, t):
    def traverse(r, s, p):
        if r:
            print(s)
            if r.val + s == t:
                print(p + [r.val])
            for n in [r.left, r.right]:
                traverse(n, r.val, [r.val])
                traverse(n, s + r.val, p + [r.val])

    traverse(root, 0, [])
