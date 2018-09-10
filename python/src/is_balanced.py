def is_balanced(root):
    def find_h(root):
        height = 0
        if root:
            height = 1 + max(find_h(root.left), find_h(root.right))
        return height

    def is_sub_balanced(root):
        balanced = True
        if root:
            balanced = is_sub_balanced(root.left)                 and \
                       is_sub_balanced(root.right)                and \
                       abs(find_h(root.left) - find_h(root.right)) <= 1
        return balanced

    return is_sub_balanced(root)
