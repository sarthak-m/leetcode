class Solution:

	def find_max_substring(self, i,s):
		substring = s[i]
		for j in range(i+1,len(s)):
			if s[j] in substring:
				return substring
			else:
				substring += s[j]

		return substring

	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		substring = []

		for i in range(0,len(s)):
			substring.append(self.find_max_substring(i,s))
		
		if len(substring) > 0:
		    return len(max(substring, key=len))
        else:
            return 0
		

def main():
	foo = Solution()
	bar = "abcabde"
	print(foo.lengthOfLongestSubstring(bar))


if __name__ == "__main__":
	main()