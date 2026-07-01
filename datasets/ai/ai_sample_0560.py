def max_sum_route(tree, start, end):
 if start == end:
 return tree[start]
 else:
 return tree[start] + max(max_sum_route(tree, start + 1, end), 
 max_sum_route(tree, start + 2, end))
 
tree = {'A':8, 'B':11, 'C':7}
start = 'A'
end = 'C'
 
ans = max_sum_route(tree, start, end)
print(ans)

#Output
23