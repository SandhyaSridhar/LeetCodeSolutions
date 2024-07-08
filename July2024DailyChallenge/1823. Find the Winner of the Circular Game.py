class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        person = [num for num in range(1,n+1,1)]
        index = 0

        while len(person)!=1:
            index = (index+k-1)%len(person)
            print(person[index])
            person.pop(index)

        return person[0]
