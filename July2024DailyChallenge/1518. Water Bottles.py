#Time Complexity: O(log N)

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            inter = numBottles % numExchange
            numBottles //= numExchange
            res += numBottles
            numBottles += inter
        return res
