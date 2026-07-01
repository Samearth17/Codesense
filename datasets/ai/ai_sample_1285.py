def longest_common_substring(s1, s2):
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    longest_len = 0
    longest_string = ""

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest_len:
                    longest_len = dp[i][j]
                    longest_string = s1[i - longest_len:i]
            else:
                dp[i][j] = 0
    return longest_string