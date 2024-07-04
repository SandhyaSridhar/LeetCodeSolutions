#Solution One
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        if c1 == c2:
            return True
        else:
            return False

#Solution Two
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for x in s:
            count[x] += 1

        for x in t:
            count[x] -= 1

        for v in count.values():
            if v != 0:
                return False

        return True
