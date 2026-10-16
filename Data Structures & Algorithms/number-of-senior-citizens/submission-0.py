class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for k in details:
            temp = k[11:13]
            if int(temp) > 60:
                count += 1
        return count