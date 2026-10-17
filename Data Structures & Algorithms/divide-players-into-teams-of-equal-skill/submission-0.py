class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        target = skill[0] + skill[-1]          # every team must hit this sum
        total = 0

        for i in range(n // 2):
            a, b = skill[i], skill[n - 1 - i]  # i-th weakest with i-th strongest
            if a + b != target:
                return -1                       # forced pairing failed, so nothing works
            total += a * b
        return total