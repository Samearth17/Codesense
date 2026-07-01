def find_valid_parens_combinations(n):
   if n == 0:
      return 0

   if n == 1:
      return 1

   combinations = 0
   for i in range(1, n, 2):
      left  = i
      right = n - i

      combinations += find_valid_parens_combinations(left) * find_valid_parens_combinations(right)

   return combinations