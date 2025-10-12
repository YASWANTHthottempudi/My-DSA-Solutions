class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        from collections import Counter

        occ = Counter(power)
        v = sorted(occ.keys())
        c = [occ[x] for x in v]

        n = len(v)
        dp = [0] * n
        dp[0] = v[0] * c[0]

        for i in range(1, n):
            take = v[i] * c[i]
            j = i - 1
            while j >= 0 and v[i] - v[j] <= 2:
                j -= 1
            if j >= 0:
                take += dp[j]
            dp[i] = max(dp[i - 1], take)

        return dp[-1]
