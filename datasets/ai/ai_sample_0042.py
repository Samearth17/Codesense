def divide_in_two_equal_parts(lst):
    target = sum(lst) // 2
    part1 = []
    part2 = []
    left_sum = 0
    right_sum = 0
    
    for num in lst:
        if left_sum <= right_sum:
            left_sum += num
            part1.append(num)
        else:
            right_sum += num
            part2.append(num)
         
    return part1, part2

part1, part2 = divide_in_two_equal_parts([2, 3, 4, 5, 6, 7])

print("Part 1:", part1)
print("Part 2:", part2)