class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index("#", i)          # find end of the length
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])  # take exactly `length` chars
            i = j + 1 + length           # jump to the next length
        return res