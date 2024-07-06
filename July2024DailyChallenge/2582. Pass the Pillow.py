class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos = 1 
        lr = True

        for i in range(1,time+1):
            if lr:
                pos+=1
            else:
                pos-=1

            if i%(n-1)==0:
                lr = not lr
            
        return pos
