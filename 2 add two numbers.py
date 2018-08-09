# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __str__(self):
		result = "[" + str(self.val)
		node = self.next
		while node != None:
			result += ","
			result += str(node.val)                
			node = node.next

		result += "]"
		return result

class Solution:
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		z = output = ListNode(0)
		carry = 0
		
		while l1 != None and l2 != None:

			if l1.next != None or l2.next != None:
				output.next = ListNode(0)

			output.val = (l1.val + l2.val + carry) % 10
			carry = int((l1.val + l2.val) / 10)

			output = output.next
			l1 = l1.next
			l2 = l2.next

		if carry > 0:
			output.next = ListNode(carry)

		return z


def main():
	foo = Solution()

	x = l1 = ListNode(2)
	l1.next = ListNode(4)
	l1 = l1.next
	l1.next = ListNode(3)

	y = l2 = ListNode(5)
	l2.next = ListNode(6)
	l2 = l2.next
	l2.next = ListNode(4)
	print(foo.addTwoNumbers(x,y))


if __name__ == "__main__":
	main()