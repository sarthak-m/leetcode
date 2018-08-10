class Solution:

	def findMedianArray(self, nums):
		size = len(nums)
		if size % 2 == 0:
			return float((nums[int(size/2)] + nums[int(size/2 -1)]) / 2)
		else:
			return nums[int(size/2)]

	def sortArrays(self, nums1, nums2):
		if nums1[-1] < nums2[0]:
			return nums1 + nums2
		elif nums2[-1] < nums1[0]:
			return nums2 + nums1
		
		nums = []
		i = 0
		j = 0
		while i < len(nums1) and j < len(nums2):
			if nums1[i] < nums2[j]:
				nums.append(nums1[i])
				i += 1
			else:
				nums.append(nums2[j])
				j += 1

		if i < len(nums1):
			nums += nums1[i:]
		if j < len(nums2):
			nums += nums2[j:]

		# print(nums)
		return nums
		
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""

		total_size = len(nums1) + len(nums2)

		if len(nums1) == 0:
			return self.findMedianArray(nums2)
		elif len(nums2) == 0:
			return self.findMedianArray(nums1)
		else:
			nums = self.sortArrays(nums1, nums2)
			return self.findMedianArray(nums)

		

def main():
	foo = Solution()
	
	nums1 = [1,2]
	nums2 = [-1,3]

	print(foo.findMedianSortedArrays(nums1, nums2))


if __name__ == "__main__":
	main()