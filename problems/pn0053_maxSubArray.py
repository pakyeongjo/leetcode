class MaxSubArray:
    def solution(self, nums):
        if len(nums) == 1:
            return nums[0]

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

    def solution2(self, nums):
        if len(nums) == 1:
            return nums[0]

        res = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums) + 1):
                res.append(sum(nums[i:j]))
        return max(res)

