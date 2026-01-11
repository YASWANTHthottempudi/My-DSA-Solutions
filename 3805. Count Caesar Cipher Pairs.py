class Solution:
    def countPairs(self, words: List[str]) -> int:
        hashes = Counter()
        for word in words:
            diffs = tuple(
                (ord(word[i]) - ord(word[0]) + 26) % 26 
                for i in range(1, len(word))
            )
            hashes[diffs] += 1

        result = 0
        for _, count in hashes.items():
            result += count * (count - 1) // 2

        return result
