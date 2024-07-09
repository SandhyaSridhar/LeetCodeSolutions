#Time Complexity: O(n)
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finale = 0
        finish = customers[0][0]
        start, wt = 0,0
        for i in range(len(customers)):
            start = customers[i][0]    
            if customers[i][0]>finish:
                finish = customers[i][0]
            finish = finish + customers[i][1]
            wt = finish - start
            finale+=wt
        
        return (finale/len(customers))
