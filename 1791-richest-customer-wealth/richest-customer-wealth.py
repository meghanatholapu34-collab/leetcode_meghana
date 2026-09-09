class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0

        for account in accounts:
            total = sum(account)
            maximum = max(maximum, total)

        return maximum      