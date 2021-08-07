class Solution:
    def __init__(self):
        self.nums = nums
        self.target = target
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                total = nums[i] + nums[j]
                if total == target:
                    x = i
                    y = j
                    #result_list = [x,y]
                    return x,y

        
if __name__ == "__main__":
    nums = input()
    nums = eval(nums)
    target = int(input())
    calc = Solution()
    result = calc.twoSum(nums,target)
    Output = [result[0],result[1]]
    print(Output)
    
        
