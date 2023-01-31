class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = nums
        for i in range(length):
            if i != 0:
                res[i] = res[i] + res[i-1]
        
        return res



if __name__ == "__main__":
    input = [1,2,3,4]
    sol = Solution()
    print(sol.runningSum(input))
