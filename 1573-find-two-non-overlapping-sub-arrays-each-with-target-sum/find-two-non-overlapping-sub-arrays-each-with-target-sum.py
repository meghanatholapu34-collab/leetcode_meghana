class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1
        dp = [INF] * (n + 1)
        seen = {0: 0}
        prefix = 0
        ans = INF
        best = INF
        for i in range(1, n + 1):
            prefix += arr[i - 1]
            # Check whether a subarray ending at i-1
            # has sum = target
            if prefix - target in seen:
                j = seen[prefix - target]
                length = i - j
                # Previous subarray ends at or before j
                if dp[j] != INF:
                    ans = min(ans, dp[j] + length)
                # Store the best single subarray
                best = min(best, length)
            dp[i] = best
            # Store current prefix sum
            if prefix not in seen:
                seen[prefix] = i
        return -1 if ans == INF else ans