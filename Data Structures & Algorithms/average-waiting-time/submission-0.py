class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        free_at = 0
        total_wait = 0

        for arrival, time in customers:
            start = max(arrival, free_at)
            free_at = start + time
            total_wait += free_at - arrival

        return total_wait / float(len(customers))