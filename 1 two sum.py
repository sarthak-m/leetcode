class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for index, number in enumerate(nums):
        	complement = target - number
        	if complement in nums and index != nums.index(complement):
        		return [index, nums.index(complement)]

        return [-1]


def main():
	foo = Solution()
	print(foo.twoSum([3,2,4], 6))

if __name__ == "__main__":
	main()