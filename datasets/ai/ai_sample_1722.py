def max_path_sum(root):
    if not root:
        return 0

    left_sum = max_path_sum(root.left)
    right_sum = max_path_sum(root.right)

    max_single_val = max(max(left_sum, right_sum) + root.data, root.data)

    max_top = max(max_single_val, left_sum + root.data + right_sum)

    max_path_sum.res = max(max_path_sum.res, max_top)

    return max_single_val

max_path_sum.res = float('-inf')
max_path_sum(root)
print (max_path_sum.res)