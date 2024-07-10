class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step = 0
        for i in logs:
            if i == '../':
                if step == 0:
                    continue
                else:
                    step -= 1
            elif i == './':
                continue
            else:
                step += 1

        return step
