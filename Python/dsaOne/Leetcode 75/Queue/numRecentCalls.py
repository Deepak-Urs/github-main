#https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75

class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t):
        while self.queue and self.queue[0] + 3000 < t:
            self.queue.pop(0)
        
        self.queue.append(t)

        return len(self.queue)


#["RecentCounter", "ping", "ping", "ping", "ping"]
#[[], [1], [100], [3001], [3002]]
obj = RecentCounter()
param_1 = obj.ping(1)

