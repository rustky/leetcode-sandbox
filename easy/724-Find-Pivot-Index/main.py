class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_len = len(nums)
        for i in range(list_len):
            left_index = i
            right_index = i + 1
            left_sum = sum(nums[:left_index])
            right_sum = sum(nums[right_index:])
            if right_sum == left_sum:
                return i
        return -1
if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    sol = Solution()
    ans = sol.pivotIndex(nums)
    print(ans)
