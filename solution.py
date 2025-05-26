class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        result = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        for p,n in zip(pos, neg):
            result.append(p)
            result.append(n)

        return result
#time complexity - O(n)
#space complexity - O(n)
