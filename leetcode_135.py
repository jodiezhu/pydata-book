
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n <= 1:
            return n
            
        # initial state: each kid gets one candy    
        nums = [1] * n
        # kids on upwards curve get candies
        for i in xrange(1, n):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1
        print(nums)
        # kids on downwards curve get candies
        # if a kid on both up/down curves, i.e. a peak or a valley
        # kid gets the maximum candies among the two.
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                nums[i-1] = max(nums[i]+1, nums[i-1])
        print(nums)
        return sum(nums)
    
s=Solution()
print(s.candy([1,3,4,2,1]))
