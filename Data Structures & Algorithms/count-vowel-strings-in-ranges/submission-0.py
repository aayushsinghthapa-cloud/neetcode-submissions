class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set ("aeiou")

        prefix = [0] * (len(words) + 1)

        for i, w in enumerate(words):
            good = w[0] in vowels and w[-1] in vowels
            prefix[i + 1] = prefix[i] + (1 if good else 0)

        return [prefix[r + 1] - prefix[l] for l, r in queries]

