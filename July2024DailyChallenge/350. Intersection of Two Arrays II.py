#Time Complexity: O(m+n)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        n = len(nums1)+len(nums2)
        freq = [0]*(1010)

        for i in nums1:
            freq[i]+=1

        for i in nums2:
            if freq[i]>0:
                res.append(i)
                freq[i]-=1

        return res
